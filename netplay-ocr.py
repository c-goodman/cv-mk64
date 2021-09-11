from logging import StringTemplateStyle
import cv2 as cv
import numpy as np
import os
from windowcapture import WindowCapture
import win32gui, win32ui, win32con
import easyocr
import pandas as pd


# # Change the working directory to the folder this script is in.
# # Doing this because I'll be putting the files from each video in their own folder on GitHub
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

reader = easyocr.Reader(lang_list=['en'])
wincap = WindowCapture("Dolphin NetPlay")
screenshot = wincap.get_screenshot()

# Crop position if hosting
crop_img = screenshot[88:497, 455:739]
# Crop position if not hosting
# crop_img = screenshot[44:497, 455:739]
simple_output = reader.readtext(crop_img, detail=0, mag_ratio=2)
        

# simple_output_testing = ['cooper[1]', '5,0 Win | 1---', 'Oms', 'connor[2]', '5,0 Win |-2-----', '8ms',
#  'cole[3]', '5.0 Win | -3---', '19ms', 'Ping:', 'Ping:', 'Ping:']

# Remove items from list that end in 'ms'
no_endswith_ms = [s for s in simple_output if not s.endswith('ms')]
# Remove items from list that end in 'ing:'
no_endswith_ing = [s for s in no_endswith_ms if not s.endswith('ing:')]

# Divide into two lists based on .startswith method
ports = [s for s in no_endswith_ing if s.startswith('5')]
players = [s for s in no_endswith_ing if not s.startswith('5')]

# Create dictionary of new lists
diction = {'Players':players, 'Ports':ports}

# Put dictionary in a Pandas DataFrame
df = pd.DataFrame(diction)

# Use .strip method to remove clutter
df['Players'] = df['Players'].str.strip('[]12345678')
df['Ports'] = df['Ports'].str.strip('5,.0 |-Win')

print(df)