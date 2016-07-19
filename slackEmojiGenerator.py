# -*- coding: utf-8 -*-
import sys
from String2emoji import String2emoji
argvs = sys.argv
argc = len(argvs)

if __name__ == '__main__':
    fontFile = 'NotoSansCJKjp-hinted/NotoSansMonoCJKjp-Bold.otf'
    text = []
    if argc == 1:
        exit()
    for num in range(1,argc):
        text.append(argvs[num])

    emoji = String2emoji(text,fontFile)

    img = emoji.getEmoji()
    saveFile = 'emoji_'
    for i in range(0,argc-1):
        saveFile += text[i].decode('mbcs')
    saveFile += '.png'
    img.save(saveFile)
