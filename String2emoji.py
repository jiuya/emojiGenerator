# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

class String2emoji(object):
    """docstring for String2emoji"""
    def __init__(self, argText,argFontName,argFontColor = (0,0,0)):
        self.textList = argText
        self.fontName = argFontName
        self.backColor = (255,255,255,0)
        self.imageSize = (128,128)
        self.fontColor = argFontColor


    def getFont(self,size):
        return ImageFont.truetype(self.fontName, size, encoding='utf-8')

    def setBackColor(self,color):
        self.backColor = color

    def setFontColor(self,color):
        self.fontColor = color
    def cutEffectiveRange(self,text,wMax,hMax):
        for i in range(hMax,hMax*2):
            font = self.getFont(i)
            w, h = font.getsize(text)
            x0 = self.stringOverBorderX(text,font)
            y0 = self.stringOverBorderY(text,font)
            x1 = self.stringUnderBorderX(text,font,x0,w)
            y1 = self.stringUnderBorderY(text,font,y0,h)
            if (y1 >= hMax-1) :
                return (i-1,x0,y0,x1,y1);
    def stringOverBorderX(self,text,font):
        for x in range(0,-128,-1):
            img = Image.new("RGBA",(128,128),self.backColor)
            draw = ImageDraw.Draw(img)
            draw.text((x,0), text.decode('mbcs'), fill=self.fontColor, font=font)
            limitFlag = 0
            for i in range(0,128):
                color = img.getpixel((0,i))
                if color != self.backColor:
                    limitFlag = 1;
            if limitFlag > 0:
                return x
    def stringOverBorderY(self,text,font):
        for y in range(0,-128,-1):
            img = Image.new("RGBA",(128,128),self.backColor)
            draw = ImageDraw.Draw(img)
            draw.text((0,y), text.decode('mbcs'), fill=self.fontColor, font=font)
            limitFlag = 0
            for i in range(0,128):
                color = img.getpixel((i,0))
                if color != self.backColor:
                    limitFlag = 1;
            if limitFlag > 0:
                return y
    def stringUnderBorderX(self,text,font,x0,w):
        img = Image.new("RGBA",(w,128),self.backColor)
        draw = ImageDraw.Draw(img)
        draw.text((x0,0), text.decode('mbcs'), fill=self.fontColor, font=font)
        for cx in range(w-1,0,-1):
            for cy in range(0,128):
                color = img.getpixel((cx,cy))
                if color != self.backColor:
                    return cx;
    def stringUnderBorderY(self,text,font,y0,h):
        img = Image.new("RGBA",(128,128),self.backColor)
        draw = ImageDraw.Draw(img)
        draw.text((0,y0), text.decode('mbcs'), self.fontColor, font=font)
        for cy in range(127,0,-1):
            for cx in range(0,128):
                color = img.getpixel((cx,cy))
                if color != self.backColor:
                    return cy;

    def getEmoji(self):
        img = Image.new("RGBA",self.imageSize,self.backColor)
        draw = ImageDraw.Draw(img)
        l = len(self.textList)
        if l == 1:
            (size,x0,y0,x1,y1) = self.cutEffectiveRange(self.textList[0],128,128)
            font = self.getFont(size)
            draw.text((x0,y0+abs(128-y1)/2), self.textList[0].decode('mbcs'), fill=self.fontColor, font=font)
            return img

        for i in range(0,l):
            img_str = Image.new("RGBA",(256,128),self.backColor)
            draw = ImageDraw.Draw(img_str)
            (size,x0,y0,x1,y1) = self.cutEffectiveRange(self.textList[i],128,128/l)
            font = self.getFont(size)
            draw.text((x0,y0), self.textList[i].decode('mbcs'), fill=self.fontColor, font=font)
            img_str.crop((0,0,x1,y1))
            if(x1 > 128):
                img_str = img_str.transform(img_str.size,Image.AFFINE,(x1/128.0,0,0,0,1,0),Image.BICUBIC)
            img.paste(img_str,(0,(128/l)*i))
        return img
