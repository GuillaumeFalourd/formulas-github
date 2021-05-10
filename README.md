[![Security Pipeline](https://github.com/GuillaumeFalourd/formulas-github/actions/workflows/security_pipeline.yml/badge.svg)](https://github.com/GuillaumeFalourd/formulas-github/actions/workflows/security_pipeline.yml)

# Ritchie Formulas Github

<img width="944" alt="title" src="https://user-images.githubusercontent.com/22433243/117589495-34453800-b100-11eb-9878-9e33af7686b4.png">

## Documentation

This repository contains Ritchie formulas which can be executed by [ritchie-cli](https://github.com/ZupIT/ritchie-cli).

- [Ritchie CLI documentation](https://docs.ritchiecli.io)
- [Step by step to create a Github profile with Ritchie CLI](https://bit.ly/devtoritgithubcreateprofile)

## Formulas available on this repository

<img width="1011" alt="repo formulas list" src="https://user-images.githubusercontent.com/22433243/117680153-4c13cf00-b187-11eb-86d8-ad2fed42b537.png">

### Repositories

- [Add Github Actions](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/add/github-actions): `rit github add github-actions`
- [Add Github Secret](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/add/secret): `rit github add secret`
- [Create Github Repository](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/create/repo): `rit github create repo`
- [Delete Github Secrets](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/delete/secrets): `rit github delete secrets`
- [Delete Github Repository](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/delete/repo): `rit github delete repo`
- [Get Github Repo Details](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/repo): `rit github get repo`
- [Get Github Repositories Insights](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/insights): `rit github get insights`
- [Create Github Branch](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/create/branch): `rit github create branch`
- [Update Github Repo Default Branch](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/update/repo/default-branch): `rit github update repo default-branch`
- [Update Many Github Repo Default Branches](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/update/many-default-branches): `rit github update many-default-branches`

### Users

- [Create Github Profile](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/create/profile): `rit github create profile`
- [Generate Github Release](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/generate/release): `rit github generate release`
- [Get Github User Details](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/user): `rit github get user`
- [Get Github User Email](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/user-email): `rit github get user-email`
- [Add Github Collaborator](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/add/collaborator): `rit github add collaborator`
- [Delete Github Collaborator](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/delete/collaborator): `rit github delete collaborator`

## Use Formulas

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/installation)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal (since CLI version 2.8.0):

```bash
rit add repo --provider="Github" --name="formulas-github" --repoUrl="https://github.com/GuillaumeFalourd/formulas-github" --priority=1
```

Finally, you can check if the repository has been imported correctly by executing the `rit list repo` command.

## Contribute to the repository with your formulas

### Creating formulas

1. Fork and clone the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Check the step by step of [how to create formulas on Ritchie](https://docs.ritchiecli.io/tutorials/formulas/how-to-create-formulas)
4. Add your formulas to the repository
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

### Updating Formulas

1. Fork and clone the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Add the cloned repository to your workspaces (`rit add workspace`) with a highest priority (for example: 1).
4. Check the step by step of [how to implement formulas on Ritchie](https://docs.ritchiecli.io/tutorials/formulas/how-to-implement-a-formula)
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

- [Contribute to Ritchie community](https://github.com/ZupIT/ritchie-formulas/blob/master/CONTRIBUTING.md)

### Contributors

<a href="https://github.com/GuillaumeFalourd/formulas-github/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=GuillaumeFalourd/formulas-github" />
</a>

(Made with [contributors-img](https://contrib.rocks))
