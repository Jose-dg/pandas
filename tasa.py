# # import gspread
import pandas as pd
from binance.client import Client
from oauth2client.service_account import ServiceAccountCredentials
from pandas import DataFrame as Df

api_secret_j = 'aIqu0LNm3ivh8HXtABRBWXCpNydyMb8goKhgX0vbjNwCYqyP0DL9mzt9RuIgzbW1'
api_key_j = 'pCDzGdx6v2YBFJlHmo2UgcVzFXQF6vLRdyQn2Vkzy9rryFOyQqSx7uWY6MhcIMIM'

client = Client(api_key_j, api_secret_j)
orders = client.get_all_orders(symbol='LTCUSDT', limit=10)
move = Df(orders)
#print(move.columns)
move.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')

#print(move)

# import requests
# import json
#
# url = "https://api.binance.com/api/v3/myTrades?symbol=LTCUSDT&timestamp=1647749828499&signature=e0e88119cdbb8f9a3620349d71dfa4373a25733d60f09af5f9602d095463a8bc"
#
# payload={}
# headers = {
#   'Content-Type': 'application/json',
#   'X-MBX-APIKEY': 'pCDzGdx6v2YBFJlHmo2UgcVzFXQF6vLRdyQn2Vkzy9rryFOyQqSx7uWY6MhcIMIM'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
# dot = Df(response)
#
# print(response)