#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import arabic_reshaper
from random import randint
from bidi.algorithm import get_display

def maker1_f(name,phone,desc,email,website):
    img = Image.open("f1.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("titr.ttf", 16, encoding='unic')
    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text_alignment = 'right';
    draw.text_antialias = True
    draw.text_encoding = 'utf-8'
    
    font = ImageFont.truetype("titr.ttf", 60, encoding='unic')
    #phone = phone.decode('utf-8')
    disp=arabic_reshaper.reshape(phone)
    disp = get_display(disp)
    draw.text((img.width / 3 -15*len(desc) +20 , img.height/2 + 400),disp,(255,255,255),font=font)


    font = ImageFont.truetype("Georgia.ttf", 46, encoding='unic')
    draw.text((img.width / 3 -10*len(email) + 700 , img.height/2 + 420),email,(255,255,255),font=font)


    font = ImageFont.truetype("titr.ttf", 110, encoding='unic')
    name=' '+name
    #name = name.decode('utf-8')
    namedisp=arabic_reshaper.reshape(name)
    namedisp = get_display(namedisp)

    w, h = draw.textsize(namedisp,font)
    draw.text(( (img.width -w)/2 , img.height/2 - 66 ),namedisp,(255,255,255),font=font)


    font = ImageFont.truetype("Yekan.ttf", 73 , encoding='unic')
    desc=' '+desc
    #desc = desc.decode('utf-8')
    descdisp=arabic_reshaper.reshape(desc)
    descdisp = get_display(descdisp)

    w, h = draw.textsize(descdisp,font)
    draw.text(( (img.width -w)/2 , img.height/2 +200),descdisp,(255,255,255),font=font)





    photoadd=str(randint(111,9876543210))+".png"
    img.save(photoadd)

    return photoadd


def maker1_b(back,backsub):
    img = Image.open("b1.png")
    draw = ImageDraw.Draw(img)
    W,H = img.size
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("titr.ttf", 16, encoding='unic')
    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text_alignment = 'right';
    draw.text_antialias = True
    draw.text_encoding = 'utf-8'
    
    font = ImageFont.truetype("Georgia.ttf", 205, encoding='unic')
    back=' '+back
    #back = back.decode('utf-8')
    #namedisp=arabic_reshaper.reshape(back)
    #namedisp = get_display(namedisp)
    w, h = draw.textsize(back,font)
  
    draw.text( ( (W-w)/2,(H-h)/2 - 250 ) ,back,(255,255,255),font=font)



    font = ImageFont.truetype("Georgia.ttf", 88, encoding='unic')
    backsub=' '+backsub
    #backsub = backsub.decode('utf-8')
    #descdisp=arabic_reshaper.reshape(backsub)
    #descdisp = get_display(descdisp)
    w, h = draw.textsize(backsub,font)
    draw.text(( (W-w)/2 , img.height/2),backsub,(255,255,255),font=font)





    photoadd=str(randint(111,9876543210))+".png"
    img.save(photoadd)

    return photoadd




