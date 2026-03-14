import requests
import json
headers = {"Api-Key": "CmYPdul8o5BwCb2M16zcTruNVHbsGPYwHmTDb7nvQGwhlRJIQh"}
url1 = "https://plant.id/api/v3/kb/plants/name_search?q=aloe vera"
res1 = requests.get(url1, headers=headers).json()
access_token = res1['entities'][0]['access_token']
url2 = f"https://plant.id/api/v3/kb/plants/{access_token}?details=image"
res2 = requests.get(url2, headers=headers).json()
print(json.dumps(res2, indent=2))
