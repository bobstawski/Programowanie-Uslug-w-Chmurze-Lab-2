import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering.authoring import AuthoringClient

endpoint = 'https://lab2-puwc-bo.cognitiveservices.azure.com/'
key = 'confidential'

client = AuthoringClient(endpoint, AzureKeyCredential(key))

project_name = "IssacNewton"
update_sources_poller = client.begin_update_sources(
    project_name=project_name,
    sources=[
        {
            "op": "add",
            "value": {
                "displayName": "Issac Newton Bio",
                "sourceUri": "https://wikipedia.org/wiki/Isaac_Newton",
                "sourceKind": "url"
            }
        }
    ]
)
update_sources_poller.result()

print("list project sources")
sources = client.list_sources(
    project_name=project_name
)
for source in sources:
    print("project: {}".format(source["displayName"]))
    print("\tsource: {}".format(source["source"]))
    print("\tsource Uri: {}".format(source["sourceUri"]))
    print("\tsource kind: {}".format(source["sourceKind"]))
