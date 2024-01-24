import argparse
import cv2
import pytesseract
from pytesseract import Output
import os


def cnv_img(img_path):
    img = cv2.imread(img_path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def extract_text(img):
    return pytesseract.image_to_string(img)