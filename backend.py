import pandas as pd
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

#Permission
f = InstalledAppFlow.from_client_secrets_file("key.json",["https://www.googleapis.com/auth/spreadsheets"])
cred = f.run_local_server(port=0)
service = build("Sheets", "v4", credentials=cred).spreadsheets().values()
d = service.get(spreadsheetId="1XhjsIQpwMcSbC1wh5EqoFs20S6pWwxgJFQicYH8PxdQ", range="A:F").execute()
data = d['values']
df = pd.DataFrame(data=data[1:], columns=data[0])
print(df)
