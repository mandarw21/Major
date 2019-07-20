# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:36:38 2019

@author: Trevor
"""

import base64 
import sys

string = ""

with open("E:/Programs/Python/images/t.png", "rb") as imageFile:
    string = base64.b64encode(imageFile.read())
    #print(string)
    print(len(string))
    print(sys.getsizeof(string))
    
# =============================================================================
# fh = open("imageToSave.png", "wb")
# fh.write(string.decode('base64'))
# fh.close()  
# =============================================================================

imgdata = base64.b64decode(string)
filename = 'some_image.png'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata) 
