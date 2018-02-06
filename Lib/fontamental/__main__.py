#!/usr/bin/env python
# encoding: utf-8

from fontamental.minify import MinifyUFO
from fontamental.maxify import MaxifyUFO
from ufo2ft import compileOTF
import argparse

def main():
    config = "./config.ini"
    mini_output = "./_mini.ufo"
    maxi_output = "./build_font.otf"
    parser = argparse.ArgumentParser(prog='fontamental')
    parser.add_argument('source', metavar='"Source Font"', type=str,  help='Source File, only UFO format supported')
    parser.add_argument('-t', nargs='?', help='master template file path')
    parser.add_argument('-c', nargs='?', help='user configuration file path')
    parser.add_argument('-o', nargs='?', help='output file')
    parser.add_argument('--minify', help='minify font', action='store_true')
    args = parser.parse_args()
    source_file = args.source
    template = args.t
    if args.c is not None:
        config = args.c
    if args.minify:
        if args.o is not None:
            mini_output = args.o
    else:
        if args.o is not None:
            maxi_output = args.o

    if args.minify:
        mini = MinifyUFO(source_file, template, config)
        ufo = mini.build()
        if ufo is not None:
            ufo.save(mini_output)
            print("Font Minified :)")
    else:
        maxi = MaxifyUFO(source_file, config)
        ufo = maxi.build()
        if ufo is not None:
            otf = compileOTF(ufo, useProductionNames=False)
            if otf is not None:
                # save generated font to file
                otf.save(maxi_output)
                print("The Font (" + maxi_output + ") created successfully !")

if __name__ == "__main__":
    main()
