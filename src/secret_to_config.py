# Get secret from Google secret-manager and put the secret in config.ini.
# Set GOOGLE_APPLICATION_CREDENTIALS or explicitly create credentials and 
# re-run the application. 
# For example: 
# export GOOGLE_APPLICATION_CREDENTIALS="/home/ubuntu/service-account-file.json"
# For more information, please see 
# https://cloud.google.com/docs/authentication/getting-started
# google secret-manager ref:
# https://cloud.google.com/secret-manager/docs/reference/libraries
# https://cloud.google.com/community/tutorials/secrets-manager-python

import os
from sys import platform
import re
import ast

from google.cloud import secretmanager

home_path = os.path.expanduser('~')
if platform == "linux" or platform == "linux2":
    service_account_path = f"{home_path}/side-project-317612-a3a9fb31513b.json"
elif platform == "darwin":
    service_account_path = f"{home_path}/key/side-project-317612-a3a9fb31513b.json"


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

project_id = "side-project-317612"
secret_id = "web_secret"
version_id = "4"
name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

client = secretmanager.SecretManagerServiceClient()
res = client.access_secret_version(request={"name": name})
payload = res.payload.data.decode("UTF-8")
secret = ast.literal_eval(payload)

top_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = f"{top_dir}/conf/config.ini"
mysql_env_path = f"{top_dir}/conf/mysql_env"

with open(config_path, "w") as f:
    f.write("[dev]\n")
    f.write(f"secret_key={os.urandom(12)}\n")
    for k, v in secret.items():
        f.write(f"{k}={v}\n")

with open(mysql_env_path, "w") as f:
    for k, v in secret.items():
        if re.match(r"MYSQL*", k):
            f.write(f"{k}={v}\n")