from pathlib import Path
import os
from os import listdir
import sys

path=""

file_name = os.path.abspath(path)

files=os.listdir(file_name)
for images in files:
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
             print(images)
