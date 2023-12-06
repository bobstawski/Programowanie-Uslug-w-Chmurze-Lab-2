import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering.authoring import AuthoringClient

endpoint = 'https://lab2-puwc-bo.cognitiveservices.azure.com/'
key = 'confidential'

client = AuthoringClient(endpoint, AzureKeyCredential(key))

project_name = "IssacNewton"

deployment_poller = client.begin_deploy_project(
    project_name=project_name,
    deployment_name="production"
)
deployment_poller.result()

deployments = client.list_deployments(
    project_name=project_name
)

print("view project deployments")
for d in deployments:
    print(d)
