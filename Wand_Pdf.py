# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:24:01 2017

@author: jtaquia
"""

from __future__ import print_function
from wand.image import Image
import os
from wand.display import display

path = os.getcwd()

print('el valor es:' + path)

with Image(filename='Page1.png') as img:
                print(img.size)
                for r in 1, 2, 3:
                    with img.clone() as i:
                        i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
                        i.rotate(90 * r)
                        i.save(filename='Page0-{0}.png'.format(r))
                        display(i)

#READ Open an image file

with Image(filename='D://Yanbal_DLO//PROYECTO COMPUTER VISION//EXTRACCION DE IMAGEN EN PDF//Page1.png') as img:
    print('width =', img.width)
    print('height =', img.height)
    
#READ A BLOB
    
with open('D://Yanbal_DLO//PROYECTO COMPUTER VISION//EXTRACCION DE IMAGEN EN PDF//033colC12.pdf') as f:
    image_binary = f.read 

with Image(blob=image_binary) as img:
    print('width =', img.width)
    print('height =', img.height)
    
# Clone an image

with Image(filename='Page1.png') as original:
    with original.clone() as converted:
        converted.format = 'jpg'
        converted.save(filename='page_JAT22.jpg')
        # operations on a converted image...
        
#CONVERT
from wand.image import Image
with Image(filename='Page1.png') as original:
    with original.convert('png') as converted:
        # operations on a converted image...
    
# RESIZE, ROTATE
    

     with Image(filename='D://Yanbal_DLO//PROYECTO COMPUTER VISION//EXTRACCION DE IMAGEN EN PDF//033colC12.pdf') as img:
         print('pages = ', len(img.sequence))
 
    with img.convert('png') as converted:
        converted.save(filename='page_kal.png')
    

 
with Image(filename='D://Yanbal_DLO//PROYECTO COMPUTER VISION//EXTRACCION DE IMAGEN EN PDF//033colC12.pdf') as img:
        print('pages = ', len(img.sequence))
 
with img.convert('png') as converted:
        converted.save(filename='pyout/page.png')
        

               