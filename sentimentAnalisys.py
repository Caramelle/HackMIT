import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
    username= "ccfdcb77-1c60-42c6-8195-cd149e3f4a63",
    password= "0TGSUHaFxcpf",
    version="2016-02-11")

print(json.dumps(tone_analyzer.tone(text='I am very happy'), indent=2))