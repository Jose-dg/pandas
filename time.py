from binance.client import Client
import pandas as pd
from pandas import DataFrame as Df
import matplotlib.pyplot as plt

api_secret = 'aIqu0LNm3ivh8HXtABRBWXCpNydyMb8goKhgX0vbjNwCYqyP0DL9mzt9RuIgzbW1'
api_key = 'pCDzGdx6v2YBFJlHmo2UgcVzFXQF6vLRdyQn2Vkzy9rryFOyQqSx7uWY6MhcIMIM'

client = Client(api_key, api_secret)
deposits = client.get_deposit_history()
withdraws = client.get_withdraw_history()

deposits_graph = Df(deposits)
deposits_graph_date = pd.to_datetime(deposits_graph['insertTime'], unit='ms')
deposits_graph_select = deposits_graph.iloc[:,[0,1,2,4,6,3]]
horizonal_stack = pd.concat([deposits_graph_select, deposits_graph_date], axis=1)
planets2 = horizonal_stack.rename(columns={'insertTime':'applyTime'})
new_df=planets2.assign(Type='Deposit')

withdraws_graph = Df(withdraws)
withdraws_graph_select = withdraws_graph.iloc[:,[1,3,8,5,6,4,7]]
new_df2=withdraws_graph_select.assign(Type='Withdraws')

trades = client.get_c2c_trade_history()
trades2 = Df(trades['data'])
trades2_date = trades2.rename(columns={'amount':'amount',
                                       'asset':'coin',
                                       'orderNumber':'network',
                                       'counterPartNickName':'address',
                                       'unitPrice':'txId',
                                       'totalPrice':'status',
                                       'createTime':'applyTime',
                                       'orderStatus':'status'})

trades2_date_snap = pd.to_datetime(trades2_date['applyTime'], unit='ms')
select_columns_P2P = trades2_date.iloc[:,[6,3,0,12,8,9]]

P2P_complete = pd.concat([select_columns_P2P, trades2_date_snap], axis=1)
new_df3=P2P_complete.assign(Type='Deposit')

vertical_stack = pd.concat([new_df, new_df2, new_df3], axis=0)
print(vertical_stack)

vertical_stack.to_csv('prueba.csv', index = False, header=True)
