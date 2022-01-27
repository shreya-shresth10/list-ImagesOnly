from pathlib import Path
import os
from os import listdir

def cwp():
    print(os.getcwd())
   
cwp()
os.chdir('D:/')
folder=cwp()


for images in os.listdir(folder):
 
    if (images.endswith(".png") or images.endswith(".jpg")
        or images.endswith(".jpeg")):
        print(images)
        
