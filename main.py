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

data_filepath = ''

datatoread_boxlist = (
(1564, 2, 1611, 30), (1645, 2, 1720, 30), (1645, 2, 1720, 30), (1785, 35, 1845, 55), (1855, 8, 1910, 25),
(1865, 35, 1915, 55), (830, 1036, 985, 1050), (830, 1053, 985, 1077))
datatoread_namelist = ('teamscore', 'kdascore', 'cscore', 'fpscount', 'timer', 'ping', 'hp', 'mana')


#
# Boxlist data
# teamscore_box = (1564, 2, 1611, 30)
# kdascore_box = (1645, 2, 1720, 30)
# csscore_box = (1755, 2, 1810, 30)
# fpscount_box = (1785, 35, 1845, 55)
# timer_box = (1855, 8, 1910, 25)
# ping_box = (1865, 35, 1915, 55)
# hp_box = (830, 1036, 985, 1050)
# mana_box = (830, 1053, 985, 1077)

class Data:
    data = ''
    time = ''
    name = ''
    inputerror = False
    datastr = ''
    box = (0, 0, 0, 0)


# def Timer():
#     img_src = ImageGrab.grab(bbox=timer_box)
#     new_size = tuple(3 * x for x in img_src.size)
#     img_src = img_src.resize(new_size, Image.ANTIALIAS)
#     text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
#     return text
#
#
# def CsScore():
#     img_src = ImageGrab.grab(bbox=csscore_box)
#     new_size = tuple(3 * x for x in img_src.size)
#     img_src = img_src.resize(new_size, Image.ANTIALIAS)
#     text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
#     return text
#
#
# def KdaScore():
#     img_src = ImageGrab.grab(bbox=kdascore_box)
#     new_size = tuple(3 * x for x in img_src.size)
#     img_src = img_src.resize(new_size, Image.ANTIALIAS)
#     text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
#     return text
#
#
# def Ping():
#     img_src = ImageGrab.grab(bbox=ping_box)
#     new_size = tuple(3 * x for x in img_src.size)
#     img_src = img_src.resize(new_size, Image.ANTIALIAS)
#     text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
#     return text
#
#
# def TeamScore():
#     img_src = ImageGrab.grab(bbox=(teamscore_box))
#     new_size = tuple(3 * x for x in img_src.size)
#     img_src = img_src.resize(new_size, Image.ANTIALIAS)
#     text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
#     return text
#
#
# def FpsCount():
#     img_src = ImageGrab.grab(bbox=fpscount_box)
#     new_size = tuple(3 * x for x in img_src.size)
#     img_src = img_src.resize(new_size, Image.ANTIALIAS)
#     text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
#     return text
#
#
# def Hp(img_src):
#     img_src = ImageGrab.grab(bbox=hp_box)
#     new_size = tuple(3 * x for x in img_src.size)
#     img_src = img_src.resize(new_size, Image.ANTIALIAS)
#     text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
#     return text
# # def RawHp():
#
#
#
# def Mana(img_src):
#     new_size = tuple(3 * x for x in img_src.size)
#     img_src = img_src.resize(new_size, Image.ANTIALIAS)
#     text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
#     return text
#
#

def GetTime():
    ctime = time.strftime("%Y_%m_%d__%H_%M", time.gmtime())
    return ctime


def CreateFile():
    name = "DATAx%s.txt" % (GetTime())
    filepath = os.path.join('D:/PERS/Python Workspace/LOLstats/Data', name)
    if not os.path.exists('D:/PERS/Python Workspace/LOLstats/Data'):
        os.makedirs('D:/PERS/Python Workspace/LOLstats/Data')
    return filepath

def CreateData():
    datalist = np.empty(shape=(0))
    for i in range(datatoread_namelist.count()):
        data = Data
        data.name = datatoread_namelist[i]
        data.box = datatoread_boxlist[i]
        datalist = np.append(datalist, data)
    return datalist


def ResizeImg(img_src):
    new_size = tuple(3 * x for x in img_src.size)
    img_src = img_src.resize(new_size, Image.ANTIALIAS)
    return img_src


def DecodeImg(img_src):
    text = pytesseract.image_to_string(img_src, lang='eng', config=tessdata_dir_config)
    return text


def RecordData(datalist):
    recorded_data = datalist
    img_src = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    for i in datalist.size:
        data = datalist[i]
        data.time = GetTime()
        cropped_img = img_src.crop(data.box)
        resized_img = ResizeImg(cropped_img)
        data.data = DecodeImg(resized_img)
        recorded_data = np.append(recorded_data, data)
    return recorded_data


def FormatedData(recorded_data):
    for i in recorded_data.size:
        str = "%s , %s , %s" % (recorded_data[i])


def WriteData(data_string, filepath):
    for i in range(datalist.size):
        f.write("%s : %s\r\n" % (data_string[0], data_string[i]))
    f.write("\r\n")
    f.close()


datalist = CreateData()

while (True):
    recorded_data = RecordData(datalist)
    formated_data = FormatedData(recorded_data)
    data_filepath = CreateFile()
    f = open(data_filepath, "a+")
    if msvcrt.kbhit():
        os._exit(0)
