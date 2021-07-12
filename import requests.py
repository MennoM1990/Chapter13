import requests
import json
from requests.models import Response


#API call
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")
response_dict = r.json()
print(response_dict.keys())

#Writing to a file
with open ('repo.txt', 'w') as outfile:
    json.dump (response_dict, outfile)




#Explore information about the repositories
print(f"repositories returned: {len(response_dict)}")