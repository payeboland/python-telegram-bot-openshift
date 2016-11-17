#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import arabic_reshaper
import random, string
from bidi.algorithm import get_display

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def maker1(name,phone,desc):
    img = Image.open("bg1.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("titr.ttf", 16, encoding='unic')
    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text_alignment = 'right';
    draw.text_antialias = True
    draw.text_encoding = 'utf-8'

    #name = name.decode('utf-8')
    disp=arabic_reshaper.reshape(name)
    disp = get_display(disp)


    photoadd=randomword(18)+".png"

    draw.text((0, 0),disp,(255,255,255),font=font)
    img.save(photoadd)

    return photoadd


