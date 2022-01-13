import pywhatkit as pywhat #library with functionality for sending messages, opening youtube videos, etc.
import subprocess
from email.message import EmailMessage
import smtplib
import webbrowser
from decouple import config

def open_camera(engine):
    subprocess.run('start microsoft.windows.camera:', shell=True)

def search_google(engine):
    search = input('Enter search here: ')
    pywhat.search(search)

def youtube(engine):
    search = input('Enter search here: ')
    pywhat.playonyt(search)

def open_slack(engine):
    subprocess.Popen("C:\Connie Mao\AppData\Local\slack")

def open_discord(engine):
    subprocess.Popen("C:\Connie Mao\AppData\Local\Discord")

def open_word(engine):
    subprocess.Popen("C:\Connie Mao\AppData\Local\slack")

def open_notepad(engine):
    subprocess.Popen('C:\Windows\notepad.exe')

def open_facebook(engine):
    webbrowser.open("https://www.facebook.com/")

def send_email(engine, receiver, subject, message):
    email = EmailMessage()
    address = config("EMAIL")
    password = config("PASSWORD")
    email['To'] = engine
    email['Subject'] = subject
    email['From'] = address
    email.set_content(message)
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(address, password)
    s.send_message(email)
    s.close()

