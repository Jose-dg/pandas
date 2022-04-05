import gspread
import pandas as pd
from binance.client import Client
from oauth2client.service_account import ServiceAccountCredentials
from pandas import DataFrame as Df

api_secret_j = 'aIqu0LNm3ivh8HXtABRBWXCpNydyMb8goKhgX0vbjNwCYqyP0DL9mzt9RuIgzbW1'
api_key_j = 'pCDzGdx6v2YBFJlHmo2UgcVzFXQF6vLRdyQn2Vkzy9rryFOyQqSx7uWY6MhcIMIM'

client = Client(api_key_j, api_secret_j)
deposits = client.get_deposit_history()
withdraws = client.get_withdraw_history()
trades = client.get_c2c_trade_history()
print(trades)
