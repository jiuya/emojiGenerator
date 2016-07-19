# -*- coding: utf-8 -*-
import sys
from String2emoji import String2emoji
argvs = sys.argv
argc = len(argvs)

if __name__ == '__main__':
    fontFile = 'NotoSansCJKjp-hinted/NotoSansMonoCJKjp-Bold.otf'
    text = []
    (r,g,b) = (0,0,0)
    if argc == 1:
        exit()
    for num in range(1,argc):
        if(argvs[num][0] == '#'):
            r = int(argvs[num][1]+argvs[num][2],16)
            g = int(argvs[num][3]+argvs[num][4],16)
            b = int(argvs[num][5]+argvs[num][6],16)
        else:
            text.append(argvs[num])

    emoji = String2emoji(text,fontFile,(r,g,b))

    img = emoji.getEmoji()
    saveFile = 'emoji_'
    for i in range(0,len(text)):
        saveFile += text[i].decode('mbcs')
    saveFile += '.png'
    img.save(saveFile)
