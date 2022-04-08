import requests
from urllib.request import urlretrieve


apiKey = 'apiKey'
print(apiKey)

def APOD():
  url = "https://api.nasa.gov/planetary/apod"
  date = 'YYYY-MM-DD'
  query = {
      'api_key':apiKey,
      'date':date,
      'hd':'True'
  }
  response = requests.get(url,params=query).json()
  print(response)
APOD()
