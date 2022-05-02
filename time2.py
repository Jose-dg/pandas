import gspread
import pandas as pd
from binance.client import Client
from oauth2client.service_account import ServiceAccountCredentials
from pandas import DataFrame as Df

api_secret_j = 'aIqu0LNm3ivh8HXtABRBWXCpNydyMb8goKhgX0vbjNwCYqyP0DL9mzt9RuIgzbW1'
api_key_j = 'pCDzGdx6v2YBFJlHmo2UgcVzFXQF6vLRdyQn2Vkzy9rryFOyQqSx7uWY6MhcIMIM'

client = Client(api_key_j, api_secret_j)
client.ping()
deposits = client.get_deposit_history()

withdraws = client.get_withdraw_history()
trades = client.get_c2c_trade_history()

deposits_graph = Df(deposits)
deposits_graph_date = pd.to_datetime(deposits_graph['insertTime'], unit='ms')
horizonal_stack = pd.concat([deposits_graph, deposits_graph_date], axis=1)
withdraws_graph = Df(withdraws)

trades2 = Df(trades['data'])
deposits_graph_date = pd.to_datetime(trades2['createTime'], unit='ms')
horizonal_stack_P2P = pd.concat([trades2, deposits_graph_date], axis=1)
ing = horizonal_stack.iloc[:, [12, 1, 0, 11, 4, 6]]
out2 = ing.assign(**{'Nominal': '0', 'Payment': '0', 'Status': '0', 'type': 'deposits'})
out3 = out2.rename(columns={'insertTime': 'date',
                            'walletType': 'commission'})
out4 = withdraws_graph.iloc[:, [7, 3, 1, 2, 5, 6]]
out5 = out4.assign(**{'Nominal': '0', 'Payment': '0', 'Status': '0', 'type': 'withdraws'})
out6 = out5.rename(columns={'applyTime': 'date',
                            'transactionFee': 'commission'})

out7 = horizonal_stack_P2P.iloc[:, [14, 3, 6, 11, 12]]
out8 = horizonal_stack_P2P.iloc[:, [8, 7, 9]]
out9 = out7.rename(columns={'createTime': 'date',
                            'asset': 'coin',
                            'counterPartNickName': 'address',
                            'transactionFee': 'address'})
out10 = out9.assign(**{'txId': '0', 'type': 'transfer'})
out11 = out8.rename(columns={'unitPrice': 'Nominal',
                             'totalPrice': 'Payment',
                             'orderStatus': 'Status'})
out12 = pd.concat([out10, out11], axis=1)

balance = pd.concat([out3, out6, out12], axis=0)
df = pd.DataFrame(data=balance)
df['date'] = df['date'].astype(str)
#print(balance)


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
client = gspread.authorize(creds)
spreadsheet = client.open('Pay Day')

# deletesheed = spreadsheet.del_worksheet('test_bin')
worksheet = spreadsheet.add_worksheet('test_bin', 200, 9)
worksheet.update([df.columns.values.tolist()] + df.values.tolist())

