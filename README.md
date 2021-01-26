# Ritchie Formulas Github

![Rit banner](/docs/img/ritchie-banner.png)

## Documentation

[Contribute to the Ritchie community](https://github.com/ZupIT/ritchie-formulas/blob/master/CONTRIBUTING.md)

This repository contains Ritchie formulas which can be executed by the [ritchie-cli](https://github.com/ZupIT/ritchie-cli).

- [Gitbook](https://docs.ritchiecli.io)

## Formulas available on this repository

- [Create Github Profile](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/create/profile)
- [Create Github Repository](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/create/repo)
- [Create Github Release](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/generate/release)
- [Get Github Repo Details](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/repo)
- [Get Github User Details](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/user)
- [Get Github User Email](https://github.com/GuillaumeFalourd/formulas-github/tree/master/github/get/user-email)

## Use Formulas

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/installation)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal:

```bash
echo '{"provider":"Github", "name":"formulas-github", "url":"https://github.com/GuillaumeFalourd/formulas-github", "priority":1}' | rit add repo --stdin
```

Finally, you can check if the repository has been imported correctly by executing the `rit list repo` command.

## Contribute to the repository with your formulas

1. Fork the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Check the step by step of [how to create formulas on Ritchie](https://docs.ritchiecli.io/getting-started/creating-formulas)
4. Add your formulas to the repository
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

