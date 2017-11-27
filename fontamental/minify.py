#!/usr/bin/env python
# encoding: utf-8

from defcon import Font, Color, Glyph, Contour
from defcon.objects.point import Point
from fontamental.aragl import *
import copy
import os

class MinifyUFO():
    def __init__(self, source, mask):
        self.sUFO = source
        self.UFO = Font()
        self.layers = {}
        if mask is not None:
            self.applyMask(mask)
        templateUFO = os.path.join(os.path.dirname(__file__), 'template.ufo')
        self.templateUFO = Font(templateUFO)

    def applyMask(self, mask):
        assert os.path.isfile(mask)
        with open(mask) as f:
            lines = f.read()
            splitRaw = lines.split("\n")
            for line in splitRaw:
                try:
                    lp = line.split()
                    rawName = lp[0]
                    maskName = lp[1]
                    RAWN2M[rawName] = maskName
                except:
                    pass

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
            self.layers.update({layerName:newLayer})
        return self.layers[layerName]


    def copyFontInfo(self):
        data = self.sUFO.getDataForSerialization()
        self.UFO.setDataFromSerialization({'info': data['info']})

    def createGlyphs(self):

        self.UFO.newGlyph('.notdef')

        for glf in RAWN2C:
            layer = 0
            glfSrc = RAWN2C[glf].split(',')
            if glf == 'arAsterisk':
                m = 1
            if glf in RAWN2M:
                try:
                    mgName = [RAWN2M[glf]]
                    glyph = Glyph()
                    glyph.copyDataFromGlyph(self.sUFO[mgName[0]])
                    glyph.name = glf
                    glyph.unicode = None
                    glyph.anchors = []
                    glyph.decomposeAllComponents()
                    if layer > 0:
                        currentLayer = self.getLayer(layer)
                        currentLayer.insertGlyph(glyph)
                    else:
                        self.UFO.insertGlyph(glyph)
                    layer += 1
                    print(g + ' found :)' + '  L ' + str(layer))
                except:
                    pass
            for g in glfSrc:
                try:
                    gCode = AGL2UV[g]
                    mgName = self.sUFO.unicodeData[gCode]
                    glyph = Glyph()
                    glyph.copyDataFromGlyph(self.sUFO[mgName[0]])
                    glyph.name = glf
                    glyph.unicode = None
                    glyph.anchors = []
                    glyph.decomposeAllComponents()
                    if layer > 0:
                        currentLayer = self.getLayer(layer)
                        currentLayer.insertGlyph(glyph)
                    else:
                        self.UFO.insertGlyph(glyph)
                    layer += 1
                    print(g + ' found :)' + '  L ' + str(layer))
                except:
                    print('x'*13 + g + ' not found in font')
                glyph = None
            if layer == 0:
                self.UFO.newGlyph(glf)

    def createAnchors(self):
        factor = self.getFactorOfUPM()
        for g in self.UFO:
            try:
                sampleGlyph = self.templateUFO[g.name]
                for point in sampleGlyph.anchors:
                    xVal = point.x * factor
                    yVal = point.y * factor
                    c = Contour()
                    c.addPoint((point.x, point.y), name=point.name, segmentType="move")
                    g.appendContour(c)
            except:
                pass

    def getFactorOfUPM(self):
        standardUPM = 2048
        sourceFontUPM = self.UFO.info.unitsPerEm
        factor = int(standardUPM) / int(sourceFontUPM)
        return factor

    def sortGlyphs(self):
        self.UFO.lib['public.glyphOrder'].sort()