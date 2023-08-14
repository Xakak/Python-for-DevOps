import os
import shutil
#move files to their respective folders according to their extensions
dir_path=""
os.chdir(dir_path)
print(os.getcwd())

files=os.listdir()

jpg_path="/home/rayan/Pictures/wallpapers/wallpaper"
otf_path="/home/rayan/Pictures/wallpapers/fonts"


for file in files:
    if file.endswith('.jpg'):
        shutil.move(file,jpg_path)
    elif file.endswith('.otf'):
        shutil.move(file,otf_path)