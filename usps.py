import requests
from urllib.parse import urlencode

def getAddressStatic(parameters): 
    
    requests.post("https://tools.usps.com/tools/app/ziplookup/zipByAddress")
    return "";