# Ritchie Formula

## Premisses

- Github Account (with generated TOKEN with repository accesses)
- You will need to set Github credentials when executing the formula or through the `rit set credential` command first.

## Command

```bash
rit github create branch
```

## Description

This formula allows the user to create a new branch remotely on a repository he can access, and to set it as default if needed.

If the repository only has one branch, it used as default to create the new one as reference.
If the repositoy has more than one branch, the user will need to choose which one to use as reference to create the new one.

## Demo

### Sample 1

<img class="special-img-class" src="/docs/img/rit-github-create-branch-1.png"/>

### Sample 2

<img class="special-img-class" src="/docs/img/rit-github-create-branch-2.png"/>
