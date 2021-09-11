import cv2 as cv
import numpy as np
import os
from windowcapture import WindowCapture
import win32gui, win32ui, win32con
import easyocr


# # Change the working directory to the folder this script is in.
# # Doing this because I'll be putting the files from each video in their own folder on GitHub
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

reader = easyocr.Reader(lang_list=['en'])
wincap = WindowCapture("Dolphin NetPlay")
screenshot = wincap.get_screenshot()
crop_img = screenshot[44:497, 455:739]
simple_output = reader.readtext(crop_img, detail=0)
        
print(simple_output)