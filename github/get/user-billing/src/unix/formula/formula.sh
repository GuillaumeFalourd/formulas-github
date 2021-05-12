#!/bin/sh

runFormula() {
  ACTIONS_JSON=`curl --silent\
    -H "Authorization: token $RIT_GITHUB_TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/users/$RIT_GITHUB_USER/settings/billing/actions`

  PACKAGES_JSON=`curl --silent\
    -H "Authorization: token $RIT_GITHUB_TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/users/$RIT_GITHUB_USER/settings/billing/packages`

  SHARED_STORAGE_JSON=`curl --silent\
    -H "Authorization: token $RIT_GITHUB_TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/users/$RIT_GITHUB_USER/settings/billing/shared-storage`

  RESULT_JSON="""
  {
    \"actions\": $ACTIONS_JSON,
    \"packages\": $PACKAGES_JSON,
    \"shared_storage\": $SHARED_STORAGE_JSON
  }
  """

  echo $RESULT_JSON | jq -M '.'
}
