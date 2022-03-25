msbackup
========

CLI for backing up remote MySQL databases locally or to AWS S3.

## Usage

Pass in full database URL, the storage driver, and the destination.

S3 Example w/ bucket name:

$ msbackup bob 54.132.1.23 employees --driver s3 bucketname

Local Example w/ local path:

$ msbackup bob 54.132.1.23 employees --driver local /var/local/db_name/backups  

---
Prerequisites
---
AWS CLI installed and configured with the correct credentials
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Access to a Remote MySQL Server allowing connections from your username and host
For help, check: https://dev.to/aissalaribi/how-to-backup-locally-a-remote-mysql-database-on-linux-5e8e

---
## Installation From Source
---
To install the package after you've cloned the repository, 
run the following command from within the project directory:

$ pip install --user -e

---
## Preparing for Development
---

Follow these steps to start developing with this project:

1. Ensure 'pip' and 'pipenv' are installed
2. Clone repository: 'git clone git@github.com:aissa-laribi/msbackup'
3. 'cd' into repository
4. Create a Virtual environment: 'python3 -m venv ./<env-name>'
5. Activate the Virtual environment:  'source <env-name>/bin/activate'
