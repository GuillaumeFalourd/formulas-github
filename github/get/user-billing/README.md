# Github Get User Billing Datas Formula

**THIS FORMULA ONLY WORKS WITH UNIX OS (SHELL)**

## Premisses

- You will need to set Github credentials when executing the formula or through the `rit set credential` command first if you want to het the email associated to your personnal account.

- The GITHUB_TOKEN needs "Update ALL user data" permission
Dependencies: `curl` and `jq`

## Command

```bash
rit github get user-billing
```

## Description

This formula will return billing details about the Github user account.

- Billing details from `actions`.
- Billing details from `packages`.
- Billing details from `shared_storage`.

## Demo

<img class="special-img-class" src="/docs/img/rit-github-get-user-billing.png"/>
