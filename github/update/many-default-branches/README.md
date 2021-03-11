# Ritchie Formula

## Premisses

- Github Account (with generated TOKEN with repository accesses)
- You will need to set Github credentials when executing the formula or through the `rit set credential` command first.

## Command

```bash
rit github update many-default-branches
```

## Description

This formula allows the user to update the default branch on many repositories.

- if the new default branch already exists on the repository, it is set as default directly.
- if the new default branch doesn't exists on the respository yet, it is created based on another branch (reference), before being set as default:
  - if there is only one branch on the repository, this branch is automatically used as reference to create the new one.
  - if there are more than one branches on the repository, the user has to choose manually which branch to use as reference to create the new one.
  
## Demo

<img class="special-img-class" src="/docs/img/rit-github-update-many-default-branches.png"/>
