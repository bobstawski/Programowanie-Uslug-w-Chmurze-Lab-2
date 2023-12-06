import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering.authoring import AuthoringClient

# get service secrets
endpoint = 'https://lab2-puwc-bo.cognitiveservices.azure.com/'
key = 'bc950c4fb0014025b22c8d09df706a2b'

# create client
client = AuthoringClient(endpoint, AzureKeyCredential(key))

project_name = "IssacNewton"

# deploy project
deployment_poller = client.begin_deploy_project(
    project_name=project_name,
    deployment_name="production"
)
deployment_poller.result()

# list all deployments
deployments = client.list_deployments(
    project_name=project_name
)

print("view project deployments")
for d in deployments:
    print(d)