import threading, time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]# Setup Google Sheets APIs
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Threading Sheet").sheet1

stop_thread = threading.Event()

def thread1():
    while not stop_thread.is_set():
        sheet.update('A3', "Hello from Thread 1")
        time.sleep(5)

def thread2():
    global t1
    while True:
        value = sheet.acell('A5').value
        if value == '1':
            stop_thread.set()
            t1.join()
            print("Restarting Thread 1")
            stop_thread.clear()
            t1 = threading.Thread(target=thread1)
            t1.start()
        time.sleep(2)

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()
