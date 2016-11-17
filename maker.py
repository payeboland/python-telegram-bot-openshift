#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import arabic_reshaper
from random import randint
from bidi.algorithm import get_display

def maker1(name,phone,desc):
    img = Image.open("bg1.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("titr.ttf", 16, encoding='unic')
    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text_alignment = 'right';
    draw.text_antialias = True
    draw.text_encoding = 'utf-8'
    
    font = ImageFont.truetype("titr.ttf", 17, encoding='unic')
    #phone = phone.decode('utf-8')
    disp=arabic_reshaper.reshape(phone)
    disp = get_display(disp)
    draw.text((5, 5),disp,(255,255,255),font=font)

    font = ImageFont.truetype("titr.ttf", 45, encoding='unic')
    name=' '+name
    #name = name.decode('utf-8')
    namedisp=arabic_reshaper.reshape(name)
    namedisp = get_display(namedisp)
    draw.text((img.width / 2 -12*len(name) , img.height/2 - 100),namedisp,(0,0,255),font=font)


    font = ImageFont.truetype("Yekan.ttf", 30, encoding='unic')
    desc=' '+desc
    #desc = desc.decode('utf-8')
    descdisp=arabic_reshaper.reshape(desc)
    descdisp = get_display(descdisp)
    draw.text((img.width / 2 -8*len(desc) , img.height/2 - 10),descdisp,(0,0,255),font=font)





    photoadd=str(randint(111,9876543210))+".png"
    img.save(photoadd)

    return photoadd


