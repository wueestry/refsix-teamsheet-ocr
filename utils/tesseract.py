import os
import sys

import pytesseract
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

import re

import cv2

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

default_path = os.path.join(os.path.dirname(__file__), "..")

test_file = os.path.join(default_path, "test", "test.png")

mask_file = os.path.join(default_path, "test", "mask.png")

mask_img = cv2.imread(mask_file)   
test_img = cv2.imread(test_file) 


img_masked = cv2.bitwise_and(src1=test_img, src2=mask_img)

#plt.imshow(img_masked)

#plt.show()

data = pytesseract.image_to_string(img_masked).split(" ")

names = []
next_new = True
for d in data:
    if next_new:
        names.append(d)
        next_new = False

    elif d.isupper():
        next_new = True

    else:
        names[-1] = f"{names[-1]} {d}"

print(names)


numbers = pytesseract.image_to_string(img_masked, config=f'--psm 6').split(" ")
number_list = []
for i, n in enumerate(numbers):
    num = re.findall(r'\d+', n)
    if len(num) != 0:
        number_list.append(int(num[0]))

print(number_list)