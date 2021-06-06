#make cookies.txt in livestreams/
#copy cookies into the file
#paste the url
#type in cookies.txt
import os
import time
import apt
print("-------------------------------------")
print("| Livestream Downloader for YouTube |")
print("|               WARNING: LINUX ONLY |")
print("|                  Starting in 2s...|")
print("-------------------------------------\n")
if os.name == 'nt':
    print("| Windows system detected. Exiting...")
    exit()
time.sleep(2)
dir = ("livestreams")
chk_folder = os.path.isdir(dir)
if not chk_folder:
    os.makedirs(dir)
    print("Created Directory : ", dir)
else:
    print("Directory \"", dir, "\" already exists. Skipped.")

cache = apt.Cache()
if cache['git'].is_installed:
    print("Git is already installed. Skipped.")
else:
    print("Installing Git...")
    os.system("sudo apt-get install git -y")

if cache['curl'].is_installed:
    print("Curl is already installed. Skipped.")
else:
    print("Installing Curl...")
    os.system("sudo apt-get install curl -y")

yt_dir = ("/usr/local/bin/youtube-dl")
yt_folder = os.path.isfile(yt_dir)
if not yt_folder:
    print("Installing youtube-dl")
    os.system("sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl")
    print("Making it executable...")
    os.system("sudo chmod a+rx /usr/local/bin/youtube-dl")
else:
    print("youtube-dl is already installed. Skipped.")
os.chdir("livestreams")
url = input("YouTube Livestream URL: ")
cookies = input("YouTube Cookies Name: ")
os.system('youtube-dl "{0}" --cookies "{1}"'.format(url,cookies))