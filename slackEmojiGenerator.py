# -*- coding: utf-8 -*-
import sys
from String2emoji import String2emoji
argvs = sys.argv
argc = len(argvs)

if __name__ == '__main__':
    fontFile = 'meiryob.ttc'
    text = []
    for num in range(1,argc):
        text.append(argvs[num])

    emoji = String2emoji(text,fontFile)

    img = emoji.getEmoji()

    img.save('test.png')
