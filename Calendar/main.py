from pprint import pprint
from GOOGLE import Create_Service

CLIENT_SECRET_FILE = 'credentials_desktop.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

