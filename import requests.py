import requests
import json
from requests.models import Response


#API call
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")
response_dict = r.json()
print(f"repositories returned: {response_dict['total_count']}")


#Writing to a readable file
readable_file = r"C:\Users\DELL\Desktop\Python Training\With Git\readable_repo_data.json"
with open (readable_file, 'w') as outfile:
    json.dump(response_dict, outfile, indent=4)


#Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned {len(repo_dicts)}")

#Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key,value in sorted(repo_dict.items()):
    print(key, value)