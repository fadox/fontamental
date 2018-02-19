#!/usr/bin/env python
# encoding: utf-8

from defcon import Font, Color, Glyph, Contour
from fontamental.objects.glyphslib import GlyphsLib
import copy
import os
import argparse



class MinifyUFO():
    def __init__(self, source, template=None, config=None):
        self.GDB = GlyphsLib(False, config)  # buildFea set to false
        self.srcUFO = self.sourceFont(source)
        self.UFO = Font()
        self.layers = {}

        if template is None:
            template = os.path.join(os.path.dirname(__file__), 'database/template.ufo')
        self.templateUFO = Font(template)

    def sourceFont(self, source):
        if source is None:
            raise Exception('font-file argument missing')

        font_type = source.split('.')[-1].lower()
        if font_type == "ufo":
            src = Font(source)
        elif font_type in  ["otf", "ttf", "woff", "woff2", "ttx", "pfa"]:
            import extractor
            src = Font()
            extractor.extractUFO(source, src)
        else:
            raise Exception('font-file in format ' + font_type + " is not supported")
        return src

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
        data = self.srcUFO.getDataForSerialization()
        self.UFO.setDataFromSerialization({'info': data['info']})

    def createGlyphs(self):

        self.UFO.newGlyph('.notdef')
        missing = ''

        for glf in self.GDB.Master2Search:
            glfUnicode = int(self.GDB.Master2Unicode[glf], 16)

            print('')
            layer = 0
            stopAt = 'arAlef.fina.la'
            glfSrc = self.GDB.Master2Search[glf].split(',')
            if glf == stopAt:
                m = 1
            log = (glf + ' ' * 50)[0:20]
            if glf in self.GDB.MAPPING:
                try:
                    mgName = [self.GDB.MAPPING[glf]]
                    glyph = Glyph()
                    glyph.copyDataFromGlyph(self.srcUFO[mgName[0]])
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
                        gCode = self.GDB.Prod2Decimal[g]
                        mgName = self.srcUFO.unicodeData[gCode]
                    except:
                        try:
                            mgName = [g]
                        except:
                            pass
                    glyph = Glyph()
                    glyph.copyDataFromGlyph(self.srcUFO[mgName[0]])
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
        factor = self.getFactorOfUPM()
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
        templateUPM = self.templateUFO.info.unitsPerEm
        sourceFontUPM = self.UFO.info.unitsPerEm
        if sourceFontUPM > templateUPM:
            factor = float(templateUPM) /  float(sourceFontUPM)
        elif templateUPM > sourceFontUPM:
            factor = float(sourceFontUPM) /float(templateUPM)
        else:
            factor = 1
        return factor

    def sortGlyphs(self):
        self.UFO.lib['public.glyphOrder'].sort()


def main():
    config = "./config.ini"
    output = "./build_font.otf"
    parser = argparse.ArgumentParser(prog='minify')

    parser.add_argument('source', metavar='"Source Font"', type=str,
                        help='Source File, supported formats: UFO, ttf, otf, woff, woff2, ttx, type1')

    parser.add_argument('-t', nargs='?', help='master template file path')
    parser.add_argument('-c', nargs='?', help='custom configuration file path')
    parser.add_argument('-o', nargs='?', help='output file path')
    args = parser.parse_args()
    source_file = args.source
    template = args.t
    if args.o is not None:
        output = args.o
    if args.c is not None:
        config = args.c
    mini = MinifyUFO(source_file, template, config)
    ufo = mini.build()
    if ufo is not None:
        ufo.save(output)
        print("Font Minified :)")

if __name__ == "__main__":
    main()
