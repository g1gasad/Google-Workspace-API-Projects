import pandas as pd
import time
from pprint import pprint
from GOOGLE import Create_Service

CLIENT_SECRET_FILE = 'credentials_desktop.json'
tasks_API_NAME = 'tasks'
tasks_API_VERSION = 'v1'
tasks_SCOPES = ["https://www.googleapis.com/auth/tasks"]
tasks_service = Create_Service(CLIENT_SECRET_FILE, tasks_API_NAME, tasks_API_VERSION, tasks_SCOPES)

sheets_API_NAME = 'sheets'
sheets_API_VERSION = 'v4'
sheets_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
sheets_service = Create_Service(CLIENT_SECRET_FILE, sheets_API_NAME, sheets_API_VERSION, sheets_SCOPES)

my_tasks_list_id = 'MDIzMjY3NDgxNTg0OTU4ODE2ODc6MDow'
games_list_id = "X08wOUJ2THZGeEhhYVRkUQ"

SPREADSHEET_ID = "1wIS4jNhBDNgmFwlu8h344NSbosh_DqEzlXVf4Nmfyko"
sheets_data = sheets_service.spreadsheets().values().get(
                            spreadsheetId=SPREADSHEET_ID,
                            range="TO DO",
                            ).execute()

df = pd.DataFrame(sheets_data['values'][1:], columns=sheets_data['values'][0])
