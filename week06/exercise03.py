import requests

url="https://nominatim.openstreetmap.org/search?q=Thessaloniki&format=json"


headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

response = requests.get(url, headers = headers )
print(response.text)


