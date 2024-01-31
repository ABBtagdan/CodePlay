#Tage

import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import math
import numpy as np

def get_sequence_from_image(filepath):

    # preprocessing using opencv
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    im = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    im2 = cv2.filter2D(im, -1, kernel)
    total = 0
    amount = 0
    for row in im:
        for pixel in row:
            amount += 1
            total += pixel
    ret, bw_im = cv2.threshold(im, total/(amount*1.3), 255, cv2.THRESH_BINARY)
    total = 0
    amount = 0
    for row in im2:
        for pixel in row:
            amount += 1
            total += pixel
    ret, bw_im2 = cv2.threshold(im2, total/(amount*1.3), 255, cv2.THRESH_BINARY)

    barcodes = decode(bw_im2)

    if not barcodes:
        return "No barcode found!"

    code_data = ''

    for barcode in barcodes:
        if barcode.type not in ["EAN13", "EAN8"]:
            continue
        else: 
            code_data = barcode.data
            if barcode.type == "EAN8":
                code_type = 8
            if barcode.type == "EAN13":
                code_type = 13
            break

    if not code_data:
        return "Not valid EAN-(13/8) barcode!"

    #EAN digit representations for each side and parity.
    left_odd = ["0001101","0011001","0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
    right = ["1110010", "1100110", "1101100", "1000010","1011100","1001110", "1010000", "1000100", "1001000", "1110100"]
    left_even = [
        "0100111", 
        "0110011", 
        "0011011", 
        "0100001", 
        "0011101", 
        "0111001", 
        "0000101", 
        "0010001", 
        "0001001", 
        "0010111"  
    ]

    # Parity patterns for ean codes, the codes first digit is the index in the list
    patterns = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 2, 1, 2, 2],
        [1, 1, 2, 2, 1, 2],
        [1, 1, 2, 2, 2, 1],
        [1, 2, 1, 1, 2, 2],
        [1, 2, 2, 1, 1, 2],
        [1, 2, 2, 2, 1, 1],
        [1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 2, 1],
        [1, 2, 2, 1, 2, 1]
    ]


    #Open clause
    binary = "101"

    #byte -> str (code-data)
    code_data = str(code_data, encoding="utf-8")

    #getting the relevant parity_pattern for the code
    pattern = patterns[int(code_data[0])]


    #Convert to ones and zeros
    Left = True
    if code_type == 13:
        code_data = code_data[1:]
    for i, c in enumerate(code_data):
        if i == math.floor(len(code_data)/2):
            print("Switched to Right at ",i)
            Left = False
            binary += "01010"
        x = int(c)
        if Left:
            if code_type == 8:
                binary += left_odd[x]
            elif code_type == 13:
                if pattern[i] == 2:
                    binary += left_even[x]
                else:
                    binary += left_odd[x]
        else:
            binary += right[x]

    #End clause
    binary += "101"


    #Convert to string of 0,1,2,3,4
    result = ""
    count = 0
    lastc = 0
    for c in binary:
        if c == "0" and lastc == 0:
            result += c
            lastc = -1
        elif c == "0" and lastc not in [0, -1]:
            result += str(count)
            count = 0
            lastc = 0
        elif c == "1":
            count += 1
            lastc = 1
            
    if count != 0: result += str(count)

    #return string
    return result


    

        
