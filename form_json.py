from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import json

endpoint = 'https://lab2-puwc-obstawski.cognitiveservices.azure.com/'
key = '2245007b86a54426af68f800df81c267'

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

with open('zdj.png', "rb") as f:
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-layout", document=f
    )
result = poller.result()

# Zapis wyników analizy do pliku JSON
with open('analysis_results_formrecognizer.json', 'w') as output_file:
    output_file.write(str(result))

# Wydobywanie tekstu z dokumentu
text_data = []
for page in result.pages:
    for line in page.lines:
        text_data.append(line.content)

# Zapis wydobytego tekstu do pliku JSON
with open('text_results.json', 'w') as text_output:
    json.dump(text_data, text_output, indent=4)
