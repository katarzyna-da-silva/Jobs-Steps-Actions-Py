# Jobs-Steps-Actions-Py

# Jobs-Steps-Actions-Py

- This repository contains a GitHub Actions workflow to demonstrate a simple pipeline with steps and actions using Python.

## Workflow Description

### Build Job
- **Step 1: Checkout Repository**
  - Uses the `actions/checkout` action to clone the repository.

- **Step 2: Copy File**
  - Copies the contents of `art-de-text.txt` to a new file specified by the `FILE_PATH` environment variable.

- **Step 3: Display File Contents**
  - Displays the contents of the copied file.

- **Step 4: Append to File**
  - Appends the text "Salut DevOps!" to the original `art-de-text.txt` file.

- **Step 5: Upload Artifact**
  - Uses the `actions/upload-artifact` action to upload the current directory as an artifact named `artifacts_download`.

- **Set up Python**
  - Uses the `actions/setup-python` action to set up Python 3.11.

- **Install Dependencies**
  - Upgrades pip, lists installed packages, and installs dependencies from `requirements.txt`.

- **Run Unit Tests**
  - Executes unit tests using the `python -m pytest` command.

- **Run colors.py**
  - Executes the `colors.py` script.

### Test Job
- **Install Ponysay**
  - Installs Ponysay for fun during testing.

- **Run Ponysay**
  - Displays a Ponysay message.

## Notes
- The `artifacts_download` artifact contains files modified during the workflow execution.
