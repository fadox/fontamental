#!/usr/bin/env python
# encoding: utf-8

from defcon import Font, Color, Glyph
from argl import *
import shutil
import copy
import os

class MinifyUFO():
    def __init__(self, source):
        self.sUFO = source
        self.UFO = Font()
        self.layers = {}

        sampleUfo = os.path.join(os.path.dirname(__file__), 'sample.ufo')
        self.sampleUFO = Font(sampleUfo)

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
                    print('         ' + g + ' not found in font')
                glyph = None
            if layer == 0:
                self.UFO.newGlyph(glf)

    def createAnchors(self):
        factor = self.getFactorOfUPM()
        for g in self.UFO:
            try:
                sampleGlyph = self.sampleUFO[g.name]
                g.anchors = copy.deepcopy(sampleGlyph.anchors)
                for point in g.anchors:
                    point.x *= factor
                    point.y *= factor
            except:
                pass

    def getFactorOfUPM(self):
        standardUPM = 1000
        sourceFontUPM = self.UFO.info.unitsPerEm
        factor = int(sourceFontUPM) / int(standardUPM)
        return factor

    def sortGlyphs(self):
        self.UFO.lib['public.glyphOrder'].sort()