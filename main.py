import numpy as np  # This module is for operating with numbers and arrays
import os
import time
import msvcrt
import cv2 as cv  # image interpreter
from PIL import ImageGrab  # This is the screencapture module
import pytesseract
from pytesseract.pytesseract import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

teamscore_box = (1564, 2, 1611, 30)
kdascore_box = (1645, 2, 1720, 30)
csscore_box = (1755, 2, 1810, 30)
fpscount_box = (1785, 35, 1845, 55)
timer_box = (1855, 8, 1910, 25)
ping_box = (1865, 35, 1915, 55)
hp_box = (830, 1036, 985, 1050)
mana_box = (830, 1053, 985, 1077)



def Timer():
    img_src = ImageGrab.grab(bbox=timer_box)
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text


def CsScore():
    img_src = ImageGrab.grab(bbox=csscore_box)
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text


def KdaScore():
    img_src = ImageGrab.grab(bbox=kdascore_box)
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text


def Ping():
    img_src = ImageGrab.grab(bbox=ping_box)
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text


def TeamScore():
    img_src = ImageGrab.grab(bbox=(teamscore_box))
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text


def FpsCount():
    img_src = ImageGrab.grab(bbox=fpscount_box)
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text


def Hp():
    img_src = ImageGrab.grab(bbox=hp_box)
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text


def Mana():
    img_src = ImageGrab.grab(bbox=mana_box)
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text



def GetTime():
    ctime = time.strftime("%Y_%m_%d__%H_%M",time.gmtime())
    return ctime

def RecordData():
    data_array = np.empty(shape=(0))
    data_array = np.append(data_array,Timer())
    data_array = np.append(data_array,Hp())
    data_array = np.append(data_array,Mana())
    data_array = np.append(data_array,Ping())
    data_array = np.append(data_array,FpsCount())
    data_array = np.append(data_array,TeamScore())
    data_array = np.append(data_array,CsScore())
    data_array = np.append(data_array,KdaScore())
    return  data_array

def CreateFile():
    name="DATAx%s.txt" % (GetTime())
    filepath = os.path.join('D:/PERS/Python Workspace/LOLstats/Data', name)
    if not os.path.exists('D:/PERS/Python Workspace/LOLstats/Data'):
        os.makedirs('D:/PERS/Python Workspace/LOLstats/Data')
    return filepath
def WriteData(data_array,filepath):

    f = open(filepath,"a+")
    for i in range(data_array.size):
        f.write("%s : %s\r\n" % (data_array[0],data_array[i]))
    f.write("\r\n")
    f.close()

counter = 0
file = CreateFile()

while (True):
    data_array = RecordData()
    WriteData(data_array,file)
    counter += 1
    print("i")
    if  msvcrt.kbhit():
        os._exit(0)
