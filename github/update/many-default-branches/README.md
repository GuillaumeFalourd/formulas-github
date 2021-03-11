# Ritchie Formula

## Premisses

- Github Account (with generated TOKEN with repository accesses)
- You will need to set Github credentials when executing the formula or through the `rit set credential` command first.

## Command

```bash
rit github update many-default-branches
```

## Description

This formula allows the user to update the default branch on many o repositories.

- if the new default branch already exists on the repository, it is set as default directly.
- if the new default branch doesn't exists on the respository yet, it is created based on another branch (reference), before being set as default.

## Demo

<img class="special-img-class" src="/docs/img/rit-github-update-many-default-branches.png"/>
