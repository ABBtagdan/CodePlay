#Tage

import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import math
# import matplotlib.pyplot as plt
import numpy as np

def get_sequence_from_image(filepath):

    # preprocessing using opencv
 # save file 
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    im = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    im2 = cv2.filter2D(im, -1, kernel)
    print(im)
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
    # zbar
    # plt.imshow(im)
    # plt.show()
    # plt.imshow(bw_im)
    # plt.show()
    # plt.imshow(im2)
    # plt.show()
    # plt.imshow(bw_im2)
    # plt.show()

    barcodes = decode(bw_im2)

    if not barcodes:
        return "No barcode found!"

    d = ''

    for barcode in barcodes:
        if barcode.type not in ["EAN13", "EAN8"]:
            continue
        else: 
            d = barcode.data
            print(barcode.type)
            if barcode.type == "EAN8":
                t = 8
            if barcode.type == "EAN13":
                t = 13
            break

    if not d:
        return "Not valid EAN-(13/8) barcode"

    left_odd = ["0001101","0011001","0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
    right = ["1110010", "1100110", "1101100", "1000010","1011100","1001110", "1010000", "1000100", "1001000", "1110100"]
    left_even = [
        "0100111",  # 0
        "0110011",  # 1
        "0011011",  # 2
        "0100001",  # 3
        "0011101",  # 4
        "0111001",  # 5
        "0000101",  # 6
        "0010001",  # 7
        "0001001",  # 8
        "0010111"   # 9
    ]

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



    binary = "101"
    print(d)
    d = str(d, encoding="utf-8")
    print(d)

    pattern = patterns[int(d[0])]
    print(pattern)
    Left = True
    if t == 13:
        d = d[1:]
    for i, c in enumerate(d):
        if i == math.floor(len(d)/2):
            print("Switched to Right at ",i)
            Left = False
            binary += "01010"
        x = int(c)
        if Left:
            if t == 8:
                binary += left_odd[x]
            elif t == 13:
                if pattern[i] == 2:
                    binary += left_even[x]
                else:
                    binary += left_odd[x]
        else:
            binary += right[x]

    binary += "101"


    print(binary)
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

    return result


# #test
# dirpath = os.getcwd()+"\\barcodes"
# print(dirpath)
# allresults = []
# for path in os.listdir(dirpath):
#     print(dirpath+"\\"+path)
#     allresults.append(get_sequence_from_file_path(dirpath+"\\"+path))

# print(allresults)


    

        
