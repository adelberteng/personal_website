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
import ast

from google.cloud import secretmanager


service_account_path = "/Users/albert/key/side-project-317612-a3a9fb31513b.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

project_id = "side-project-317612"
secret_id = "web_secret"
version_id = "3"
name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

client = secretmanager.SecretManagerServiceClient()
res = client.access_secret_version(request={"name": name})
payload = res.payload.data.decode("UTF-8")
secret = ast.literal_eval(payload)

top_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = f"{top_dir}/conf/config.ini"

with open(config_path, "w") as f:
	f.write("[dev]\n")
	for k, v in secret.items():
		f.write(f"{k} = {v}\n")