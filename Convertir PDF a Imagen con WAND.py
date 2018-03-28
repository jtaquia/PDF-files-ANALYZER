# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:29:40 2018

@author: jtaquia
"""

from __future__ import print_function
from wand.image import Image
import os


print(os.getcwd())
 
with Image(filename='D://Yanbal_DLO//PROYECTO COMPUTER VISION//EXTRACCION DE IMAGEN EN PDF//033colC12.pdf') as img:
    print('pages = ', len(img.sequence))
 
    with img.convert('png') as converted:
        converted.save(filename='pageMari100.png')
        
        
        