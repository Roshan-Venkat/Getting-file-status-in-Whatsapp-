import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/spreadsheets']

CLIENT_SECRET_FILE = 'myproject-13062000-31ad06093c6d.json'


# ----------------------------------------------------------------------------------------------------------------------#
#    Establish Connection with Google API's via client_secret.json file resides in src directory
# ----------------------------------------------------------------------------------------------------------------------#
def get_google_api_connection():
   credential_path = os.path.join(CURRENT_DIR, CLIENT_SECRET_FILE)
   credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_path, SCOPES)
   google_connection = gspread.authorize(credentials)
   SHEET_ID = '1C-F1WuqIcDXpfgWnpRlPuVsBPRU0dxrDUsETaZHlYMg'
   SHEET_NAME = 'Source_file_details'
   googlesheetdata = google_connection.open_by_key(SHEET_ID).worksheet(SHEET_NAME).get_all_values()
   print(googlesheetdata)

get_google_api_connection()
