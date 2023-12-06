import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering.authoring import AuthoringClient

# get service secrets
endpoint = 'https://lab2-puwc-bo.cognitiveservices.azure.com/'
key = 'bc950c4fb0014025b22c8d09df706a2b'

# create client
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

# list sources
print("list project sources")
sources = client.list_sources(
    project_name=project_name
)
for source in sources:
    print("project: {}".format(source["displayName"]))
    print("\tsource: {}".format(source["source"]))
    print("\tsource Uri: {}".format(source["sourceUri"]))
    print("\tsource kind: {}".format(source["sourceKind"]))