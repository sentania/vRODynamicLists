import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def handler(context, inputs):
    result = 'test'
    print(result)
    return result
