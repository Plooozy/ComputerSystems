import requests # You need to install this packege in order to use it

with open("my_api.txt", "r", encoding="utf-8") as f: # here I use my API key, you can create yor own file "my_api.txt" and paste there your API
    API_KEY = f.read().strip()


address = "Moscow"
url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)
print(API_KEY)