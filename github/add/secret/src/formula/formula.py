#!/usr/bin/python3
import requests
import json
from base64 import b64encode
from nacl import encoding, public

def run(token, owner, repository, secret_name, secret_value):
    url_public_key = f"https://api.github.com/repos/{owner}/{repository}/actions/secrets/public-key"

    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r = requests.get(
        url = url_public_key,
        headers = headers
        )

    if r.status_code == 200:
        key_datas = r.json()

        url_secret = f"https://api.github.com/repos/{owner}/{repository}/actions/secrets/{secret_name}"

        data = {}
        data["encrypted_value"] = encrypt(key_datas["key"], secret_value)
        data["key_id"] = key_datas["key_id"]

        json_data = json.dumps(data)

        r = requests.put(
            url = url_secret,
            data = json_data,
            headers = headers
            )

        if r.status_code == 201 or r.status_code == 204:
            print(f"✅ Secret \033[36m{secret_name}\033[0m successfully added to {owner}'s \033[36m{repository}\033[0m repository")

        else:
            print("❌ Couldn't add the secret to the repository")
            print (r.status_code, r.reason)

    else:
        print("❌ Couldn't get the repository public key")
        print (r.status_code, r.reason)

def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")