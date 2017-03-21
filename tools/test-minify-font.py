#!/usr/bin/env python
# encoding: utf-8

from defcon import Font
from fontamental.minify import MinifyUFO
from ufo2ft import compileOTF
import shutil


def main(source, mask = None):
    mini =  MinifyUFO(source, mask)
    return mini.build()

if __name__  == "__main__":
    path = "/hub/sandbox/sources/"
    sourcePaths = ["", "lots.ufo", "adobe.ufo", "ali.ufo", 'old.ufo','old_alwand.ufo','raw_hasan.ufo']
    fontName = sourcePaths[6]
    sourceFont = Font(path + fontName)
    mask = path + 'old_ali.mask'
    ufo = main(sourceFont, mask)

    outputFilePath = path + 'mini_' +fontName

    try:
        shutil.rmtree(outputFilePath)
        print(outputFilePath + " Deleted!")
    except:
        pass

    ufo.save(outputFilePath)

    #otf = compileOTF(ufo)

    #otf = subsetGlyphs(otf, ufo)

    #otf.save(outputFilePath + '.otf')



