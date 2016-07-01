# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import sys

argvs = sys.argv
argc = len(argvs)

if __name__ == '__main__':
    bsize = 170
    fontFile = 'meiryo.ttc'
    font = ImageFont.truetype(fontFile, bsize/argc, encoding='utf-8')
    text = []

    for num in range(1,argc):
        text.append(argvs[num])

    w, h = font.getsize(text[0])
    print '%s w:%d h:%d' % (text, w, h)

    img = Image.new("RGBA",(128,128),(255,255,255))
    draw = ImageDraw.Draw(img)
    y = 0
    for t in text:
        draw.text((abs(bsize*2-w)/argc,y*(bsize/argc)-bsize*0.05), t.decode('mbcs'), fill=(0,0,0), font=font)
        y = y + 1

    img.save('test.png')
