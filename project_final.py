import datetime
import time
import os
from twilio.rest import Client
import gspread
Counter = 0
S_no = 1
content = ""
from oauth2client.service_account import ServiceAccountCredentials
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/spreadsheets']

CLIENT_SECRET_FILE = 'myproject-13062000-31ad06093c6d.json'

def get_google_api_connection():
   global S_no
   global starting_time
   global content
   credential_path = os.path.join(CURRENT_DIR, CLIENT_SECRET_FILE)
   credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_path, SCOPES)
   google_connection = gspread.authorize(credentials)
   SHEET_ID = '1C-F1WuqIcDXpfgWnpRlPuVsBPRU0dxrDUsETaZHlYMg'
   SHEET_NAME = 'Source_file_details'
   googlesheetdata = google_connection.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

   if S_no == 1:
       row= ["S.no","starting_time","Directory","Total_lines","Time_of_arrival","status"]
       googlesheetdata.insert_row(row,1)
   content = str(datetime.datetime.now())
   googlesheetdata.update_cell(2, 1, S_no)
   googlesheetdata.update_cell(2, 2, starting_time)
   googlesheetdata.update_cell(2, 3, "C:/Users/Roshan/PycharmProjects/Handson/bin/input/")
   googlesheetdata.update_cell(2, 4, Counter)
   googlesheetdata.update_cell(2, 5, content)
   googlesheetdata.update_cell(2, 6, "accepted")
def ToDo():
    global content
    try:
        CONFIG_FILE = "../data2/input/source.txt"
        file_stats = os.stat(CONFIG_FILE)
        if file_stats.st_size == 0:
            print("File detected.......")
            print("NO contents present.......")
            return 0
        else:
            print("file detected.....")
            print("processing........")
            global Counter
            file = open(CONFIG_FILE, "r")
            Content = file.read()
            CoList = Content.split("\n")
            for i in CoList:
                if i:
                    Counter += 1
            get_google_api_connection()

            TWILIO_ACCOUNT_SID = 'AC491bba6dab0eb62501753d82ad5be317'
            TWILIO_AUTH_TOKEN = '4a869ecc67b81b9888392c3a80571365'
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

            from_whatsapp_number = 'whatsapp:+14155238886'
            to_whatsapp_number = 'whatsapp:+918825759569'
            result = "STARTING TIME :" + starting_time +" | " + " FILE ARRIVED AT : C:/Users/Roshan/PycharmProjects/Handson/bin/input/" + " | "  + "NO.OF LINES IN FILE :" + str(Counter) + " | "+ " ARRIVING TIME :" + content + " | "  + " STATUS : Accepted"
            client.messages.create(body = result,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
            return 1
    except IOError:
        print("File doesn't exist......!!!!!!!")
        print("let's wait.........")
        return 0
starting_time = ""
if __name__ == '__main__':
    starting_time = str(datetime.datetime.now())
    while True:
        print("attempting to read file......")
        a = ToDo()
        if a == 0:
            time.sleep(10)
            print("trying again")
        else:
            print("success")
            break