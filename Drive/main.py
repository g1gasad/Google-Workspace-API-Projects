from GOOGLE import Create_Service
import pandas as pd

CLIENT_SECRET_FILE = 'E:\Projects\GCP Integration\credentials_desktop.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

gst_folder_id = '1ansBF8l6Kke4Ue4aRr0B1DkVx_r1ebwP'
workorder_folder_id = '1VPu6Le45nKZe9-Nzg9csCyDksdQxCqtn'

def get_data_on_all_files(FOLDER_ID, service):
    query = f"parents = '{FOLDER_ID}'"
    response = service.files().list(q=query).execute()
    files = response.get('files')
    nextPageToken = response.get("nextPageToken")
    i = 1
    while nextPageToken:
        response = service.files().list(q=query, pageToken=nextPageToken).execute()  # Include pageToken
        files.extend(response.get('files'))
        nextPageToken = response.get('nextPageToken')
    data = pd.DataFrame(files)
    return data

df = get_data_on_all_files(workorder_folder_id, service) 
df.to_excel("Trial.xlsx", index=False)
print(df.shape)

# Deletes duplicate files
def delete_duplicates(data):
    duplicate_file_id_list = list(data[data['name'].duplicated(keep='last')]['id'])
    file_to_trash = {'trashed': True}
    i = 1
    for FILE_ID in duplicate_file_id_list:
        print(i)
        service.files().update(fileId=FILE_ID, body=file_to_trash).execute()
        i = i + 1
    return "Deletion Successful"

# delete_duplicates(df)
