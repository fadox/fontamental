#!/usr/bin/env python
# encoding: utf-8

from defcon import Font
from fontamental.maxify import MaxifyUFO
import shutil


def main(source):
    font =  MaxifyUFO(source)
    return font.build()

if __name__  == "__main__":
    path = "/hub/sandbox/sources/"
    sourcePaths = ["", "mini_lots.ufo", "mini_adobe.ufo", "mini_ali.ufo", 'mini_old.ufo', 'raw_ali_alwand_regular.ufo','raw_ali_hasan_regular.ufo']
    fontName = sourcePaths[6]
    sourceFont = Font(path + fontName)

    ufo = main(sourceFont)

    outputFilePath = path + 'final_' +fontName

    try:
        shutil.rmtree(outputFilePath)
        print(outputFilePath + " Deleted!")
    except:
        pass

    ufo.save(outputFilePath)

