# Ritchie Formulas Github

![Rit banner](/docs/img/ritchie-banner.png)

## Documentation

This repository contains Ritchie formulas which can be executed by [ritchie-cli](https://github.com/ZupIT/ritchie-cli).

- [Ritchie CLI documentation](https://docs.ritchiecli.io)
- [Step by step to create a Github profile with Ritchie CLI](https://bit.ly/devtoritgithubcreateprofile)

## Formulas available on this repository

- [Create Github Profile](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/create/profile): `rit github create profile`
- [Create Github Repository](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/create/repo): `rit github create repo`
- [Delete Github Repository](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/delete/repo): `rit github delete repo`
- [Generate Github Release](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/generate/release): `rit github generate release`
- [Get Github Repo Details](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/repo): `rit github get repo`
- [Get Github User Details](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/user): `rit github get user`
- [Get Github User Email](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/user-email): `rit github get user-email`

## Use Formulas

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/installation)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal:

Via STDIN:

```bash
echo '{"provider":"Github", "name":"formulas-github", "repoUrl":"https://github.com/GuillaumeFalourd/formulas-github", "priority":1}' | rit add repo --stdin
```

ou, a partir da versão 2.9.0 do CLI, via INPUT FLAGS:

```bash
rit add repo --provider=Github --name=formulas-github --repoUrl=https://github.com/GuillaumeFalourd/formulas-github --priority=1
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
