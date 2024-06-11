import sys
import time
import random
import os
import shutil
from watchdog.observes import Observer
from watchdog.events import FileSystemEventHandle
fromdir = "C:\Users\sofil\Downloads"
todir = "C:\Users\sofil\Desktop\downloadsFiles"
dirextension = {
    "imagenfiles":[".jpg",".jpeg",".png",".gif",".jfif"],
    "videofiles":[".mp4",".mp3",".avi",".mpg",".mov"],
    "documentfiles":[".ppt",".xlc",".xlsx",".csv",".pdf",".text"],
    "setupfiles":[".exe",".bin",".cmd",".msi"]
}

class FileMoveHandler(FileSystemEventHandle):
    def on_created(self,event):
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dirextension.items():
            time.sleep(1)
            if extension in value:
                filename = os.path.basename(event.src_path)
                print("descargando"+ filename)
                path1 = fromdir + "/" + filename
                path2 = todir + "/" + key
                path3 = todir + "/" + key + "/" + filename

                if os.path.exists(path2):
                    print("moviendo"+ filename + "..")
                    shutil.move(path1,path3) 
                    time.sleep(1)
                else:
                    os.makedirs(path2)
                    print("moviendo"+ filename + "..")
                    shutil.move(path1,path3) 
                    time.sleep(1)

event_handle = FileMoveHandler()
observe = Observer()
observe.schedule(event_handle,fromdir,recursive = True)
observe.start()
try:
    while True:
        time.sleep(2)
        print("ejecutado")
except KeyboardInterrupt:
    print("detenido")
    observe.stop()