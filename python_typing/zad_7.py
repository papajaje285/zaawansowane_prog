import requests
url = "https://api.openbrewerydb.org/v1/breweries"
params = "?limit=1"

url = url + params
response = requests.get(url)
print (response.content)