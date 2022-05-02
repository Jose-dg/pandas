import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
client = gspread.authorize(creds)
spreadsheet = client.open('Pay Day')
worksheet = spreadsheet.add_worksheet('test2', 1000, 1000)


worksheet.update([df.columns.values.tolist()] + df.values.tolist())

