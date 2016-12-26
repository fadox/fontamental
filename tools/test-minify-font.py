#!/usr/bin/env python
# encoding: utf-8

from defcon import Font
from fontamental.minify import MinifyUFO
import shutil


def main(source):
    mini =  MinifyUFO(source)
    return mini.build()

if __name__  == "__main__":
    path = "/hub/sandbox/sources/"
    sourcePaths = ["", "lots.ufo", "adobe.ufo"]
    fontName = sourcePaths[1]
    sourceFont = Font(path + fontName)

    ufo = main(sourceFont)

    outputFilePath = path + 'mini_' +fontName

    try:
        shutil.rmtree(outputFilePath)
        print(outputFilePath + " Deleted!")
    except:
        pass

    ufo.save(outputFilePath)

