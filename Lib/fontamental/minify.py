#!/usr/bin/env python
# encoding: utf-8

from defcon import Font, Color, Glyph, Contour
from fontamental.glyphslib import GlyphsLib
import copy
import os
import argparse


class MinifyUFO():
    def __init__(self, source, template=None, config=None):
        self.gl = GlyphsLib(False, config)  # buildFea set to false
        self.sUFO = Font(source)
        self.UFO = Font()
        self.layers = {}

        if template is None:
            template = os.path.join(os.path.dirname(__file__), 'template.ufo')
        self.templateUFO = Font(template)

    def build(self):
        self.copyFontInfo()
        self.createGlyphs()
        self.createAnchors()
        self.sortGlyphs()
        return self.UFO

    def getLayer(self, layer):
        layerName = "BG_layer_" + str(layer)
        if layerName not in self.layers.keys():
            newLayer = self.UFO.layers.newLayer(layerName)
            newLayer.color = Color("0,1,0,1")
            self.layers.update({layerName: newLayer})
        return self.layers[layerName]

    def copyFontInfo(self):
        data = self.sUFO.getDataForSerialization()
        self.UFO.setDataFromSerialization({'info': data['info']})

    def createGlyphs(self):

        self.UFO.newGlyph('.notdef')
        missing = ''

        for glf in self.gl.RAWN2C:
            glfUnicode = int(self.gl.RAWN2U[glf], 16)

            print('')
            layer = 0
            stopAt = 'arAlef.fina.la'
            glfSrc = self.gl.RAWN2C[glf].split(',')
            if glf == stopAt:
                m = 1
            log = (glf + ' ' * 50)[0:20]
            if glf in self.gl.RAWN2M:
                try:
                    mgName = [self.gl.RAWN2M[glf]]
                    glyph = Glyph()
                    glyph.copyDataFromGlyph(self.sUFO[mgName[0]])
                    glyph.name = glf
                    if layer == 0:
                        glyph.unicode = glfUnicode
                        glyph.unicodes = [glfUnicode]
                    else:
                        glyph.unicode = None
                    glyph.anchors = []
                    glyph.decomposeAllComponents()
                    if layer > 0:
                        currentLayer = self.getLayer(layer)
                        currentLayer.insertGlyph(glyph)
                    else:
                        self.UFO.insertGlyph(glyph)
                    layer += 1
                    # print(g + ' found :)' + '  L ' + str(layer))

                    gLog = log + (mgName[0] + ' ' * 50)[0:20]
                    print(gLog + '[' + str(layer) + ']  *')
                except:
                    pass
            for g in glfSrc:
                mgName = None
                gCode = None
                gLog = log + (g + ' ' * 50)[0:20]

                try:
                    try:
                        gCode = self.gl.AGL2UV[g]
                        mgName = self.sUFO.unicodeData[gCode]
                    except:
                        try:
                            mgName = [g]
                        except:
                            pass
                    glyph = Glyph()
                    glyph.copyDataFromGlyph(self.sUFO[mgName[0]])
                    glyph.name = glf
                    if layer == 0:
                        glyph.unicode = glfUnicode
                        glyph.unicodes = [glfUnicode]
                    else:
                        glyph.unicode = None
                    glyph.anchors = []
                    glyph.decomposeAllComponents()
                    if layer > 0:
                        currentLayer = self.getLayer(layer)
                        currentLayer.insertGlyph(glyph)
                    else:
                        self.UFO.insertGlyph(glyph)
                    layer += 1
                    print(gLog + '[' + str(layer) + ']')
                except:
                    print(gLog + '[ ]')
                glyph = None
            if layer == 0:
                self.UFO.newGlyph(glf)
                missing += log + "\n"
        if len(missing) > 1:
            print('\n')
            print('=' * 60)
            print('Missing glyphes    ' + str(len(missing.splitlines())))
            print('=' * 60)
            print(missing)
            print('=' * 60)

    def createAnchors(self):
        factor = int(self.getFactorOfUPM())
        for g in self.UFO:
            try:
                sampleGlyph = self.templateUFO[g.name]
                g.anchors = copy.deepcopy(sampleGlyph.anchors)
                for point in g.anchors:
                    point.x *= factor
                    point.y *= factor
                for point in sampleGlyph.anchors:
                    xVal = point.x * factor
                    yVal = point.y * factor
                    c = Contour()
                    c.addPoint((xVal, yVal), name=point.name, segmentType="move")
                    g.appendContour(c)
            except:
                pass

    def getFactorOfUPM(self):
        standardUPM = 2048
        sourceFontUPM = self.UFO.info.unitsPerEm
        factor = float(standardUPM) / float(sourceFontUPM)
        return factor

    def sortGlyphs(self):
        self.UFO.lib['public.glyphOrder'].sort()


def main():
    source_file = None
    template = None
    config = None
    output = "./mini.ufo"
    source_path = os.getcwd()

    if os.path.isfile(source_path + os.sep + 'config.py'):
        config = source_path + os.sep + 'config.py'

    parser = argparse.ArgumentParser(prog='minify')
    parser.add_argument('source', metavar='"Source Font"', type=str,
                        help='Source File, only UFO format supported')
    parser.add_argument('-t', nargs='?', help='master template file path')
    parser.add_argument('-c', nargs='?', help='custom configuration file path')
    parser.add_argument('-o', nargs='?', help='output file path')

    args = parser.parse_args()

    if args.o is not None:
        output = args.o
    source_file = args.source
    template = args.t
    if args.c is not None:
        config = args.c

    mini = MinifyUFO(source_file, template, config)

    ufo = mini.build()

    if ufo is not None:
        ufo.save(output)
        print("Font Minified :)")


if __name__ == "__main__":
    main()
