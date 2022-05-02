import requests
# import json

url = "https://api.binance.com/sapi/v1/capital/deposit/hisrec?timestamp=1647237460260&signature=c52d4c931349611fbf986acc8ac5b4422d1a7fff78164ecb140607dd909053a0"

payload={}
headers = {
  'Content-Type': 'application/json',
  'X-MBX-APIKEY': 'pCDzGdx6v2YBFJlHmo2UgcVzFXQF6vLRdyQn2Vkzy9rryFOyQqSx7uWY6MhcIMIM'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)