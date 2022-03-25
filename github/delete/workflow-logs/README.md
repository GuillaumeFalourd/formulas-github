# Ritchie Formula

## Premisses

- Github Account (with generated TOKEN with repository accesses).
- You will need to set Github credentials when executing the formula or through the `rit set credential` command first.

## Command

```bash
rit github trigger workflow
```

## Description

Formula to trigger through a command line a Github Actions workflow using a `repository_dispatch` or a `workflow_dispatch` event, on any repository the user has access to, with or without `client_payload` / inputs.

For the `workflow_dispatch` type, the formula allows to select the workflow and the branch to trigger during the command execution.

## Demo

### 1️⃣ Repository Dispatch without `client_payload`

<img width="1050" alt="no client payload formula" src="https://user-images.githubusercontent.com/22433243/138753550-77514ffb-cc8d-43c7-9f5a-001b655cb976.png">

<img width="1421" alt="no client payload" src="https://user-images.githubusercontent.com/22433243/138753561-220b4b62-9fa5-4619-bf4a-b3dea4b402ee.png">

* * *

### 2️⃣ Repository Dispatch with `client_payload`

<img width="1059" alt="client payload formula" src="https://user-images.githubusercontent.com/22433243/138753580-25bfc16f-dcf6-45d9-9d41-616ed29f0444.png">

<img width="1423" alt="client payload" src="https://user-images.githubusercontent.com/22433243/138753591-ad9fa656-ad5b-4e3e-b52a-ea148fb21d45.png">

* * *

### 3️⃣ Workflow Dispatch without inputs

<img width="1253" alt="workflow dipatch no input formula" src="https://user-images.githubusercontent.com/22433243/138753663-11346e8a-a0af-4943-a359-50fed0f98ec4.png">

<img width="1434" alt="workflow dipatch no input" src="https://user-images.githubusercontent.com/22433243/138753679-cfd10584-3185-4aeb-8131-2fe12d6b995c.png">

* * *

### 4️⃣ Workflow Dispatch with inputs

<img width="1268" alt="workflow dipatch input formula" src="https://user-images.githubusercontent.com/22433243/138753710-5355872f-5a02-4301-8369-ec681d3f06b8.png">

<img width="1437" alt="workflow dipatch input" src="https://user-images.githubusercontent.com/22433243/138753730-b77beafa-192f-429d-a5e3-5298b7a3ada3.png">
