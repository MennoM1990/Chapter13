import json
import requests
from requests.api import head
from requests.models import Response

data = {"resources":{"core":{"limit":60,"remaining":60,"reset":1626099681,"used":0,"resource":"core"},"graphql":{"limit":0,"remaining":0,"reset":1626099681,"used":0,"resource":"graphql"},"integration_manifest":{"limit":5000,"remaining":5000,"reset":1626099681,"used":0,"resource":"integration_manifest"},"search":{"limit":10,"remaining":10,"reset":1626096141,"used":0,"resource":"search"}},"rate":{"limit":60,"remaining":60,"reset":1626099681,"used":0,"resource":"core"}}

readable_file = r"C:\Users\DELL\Desktop\Python Training\With Git\readable_rate_limit.json"
with open (readable_file, 'w') as outfile:
    json.dump(data, outfile, indent=4)