#!/usr/bin/env python
# encoding: utf-8

from defcon import Font, Color, Glyph, Contour
from fontamental.aragl import *
import copy
import os

class MaxifyUFO():
    def __init__(self, source):
        self.sUFO = source
        self.UFO = Font()
    def build(self):
        self.copyFontInfo()
        self.createGlyphs()
        self.sortGlyphs()
        return self.UFO

    def copyFontInfo(self):
        data = self.sUFO.getDataForSerialization()
        self.UFO.setDataFromSerialization({'info': data['info']})

    def createGlyphs(self):

        self.copyFundamentals()

        subs = self.getSubsets()

        for gName, pgNames in subs.items():
            if gName == 'uni0688':
                m = 1
            try:
                baseGlyph = self.UFO[pgNames[0]]

                if not gName in self.UFO.keys():
                    glyph = self.addGlyph(gName, baseGlyph)

                if len(pgNames) == 1:
                    pass
                else:
                    for partName in pgNames[1:]:
                        partGlyph = self.UFO[partName]
                        partAnchors = [a.name.replace("_", "", 1) for a in partGlyph.anchors if a.name.startswith("_")]
                        baseAnchors = [a.name for a in baseGlyph.anchors if not a.name.startswith("_")]
                        anchorName = set(baseAnchors).intersection(partAnchors)
                        assert len(anchorName) > 0, (pgNames[0], partName, partAnchors, baseAnchors)
                        anchorName = list(anchorName)[0]
                        partAnchor = [a for a in partGlyph.anchors if a.name == "_" + anchorName][0]
                        baseAnchor = [a for a in baseGlyph.anchors if a.name == anchorName][0]
                        xoff = baseAnchor.x - partAnchor.x
                        yoff = baseAnchor.y - partAnchor.y
                        self.addComponent(glyph, partName, xoff, yoff)
                        self.updateAnchors(glyph, partGlyph, xoff, yoff)
                        del baseAnchor, baseAnchors, a, xoff, yoff, partGlyph, anchorName

            except:
                pass



    def getSubsets(self):
        subs = {}
        for gName, pgNames in AGL2FEA.items():
            rep = []
            for el in pgNames:
                rep.append(self.getUniName(el))
            subs[gName] = rep
        return subs

    def getUniName(self, name):
        if name in RAWN2G:
            return RAWN2G[name]
        else:
            return name

    def addGlyph(self, gName, baseGlyph):
        glyph = self.UFO.newGlyph(gName)
        if gName in AGL2UV:
            glyph.unicode = AGL2UV[gName]
        glyph.width = baseGlyph.width
        glyph.leftMargin = baseGlyph.leftMargin
        glyph.rightMargin = baseGlyph.rightMargin
        self.addComponent(glyph, baseGlyph.name)
        self.addAnchors(glyph, baseGlyph)
        return glyph

    def copyFundamentals(self):
        for g in self.sUFO:
            if g.name in RAWN2U:
                gName = RAWN2G[g.name]
                gUnicode = int(RAWN2U[g.name], 16)
                g.name = gName
                g.unicode = gUnicode
                ng = copy.deepcopy(g)
                #ng.clearAnchors()
                self.addAnchors(ng,g)
                self.UFO.insertGlyph(ng)

    def addComponent(self, glyph, name, xoff=0, yoff=0):
        component = glyph.instantiateComponent()
        component.baseGlyph = name
        component.move((xoff, yoff))
        glyph.appendComponent(component)

    def addAnchors(self, glyph, base):
        anchors = base.anchors
        if len(anchors):
            for anchor in anchors:
                if anchor.name in ['markAbove', 'markBelow', 'markAbove_1', 'markAbove_2', 'markBelow_1',
                                   'markBelow_2','_markAbove', '_markBelow', '_markAbove_1', '_markAbove_2',
                                   '_markBelow_1',  '_markBelow_2'#, '_markAboveDot','_markBelowDot','markAboveDot','markBelowDot'
                                    ]:
                    #anc = glyph.instantiateAnchor()
                    #anc.x = anchor.x
                    #anc.y = anchor.y
                    #anc.name = anchor.name
                    #glyph.appendAnchor(anc)

                    c = Contour()
                    c.addPoint((anchor.x, anchor.y), name=anchor.name, segmentType="move")
                    glyph.appendContour(c)

                else:
                    continue

    def updateAnchors(self, glyph, base, x, y):
        anchors = base.anchors
        if len(anchors):
            for anchor in anchors:
                if anchor.name == 'markAbove' or anchor.name == 'markAboveDot':
                    for ganchor in glyph.anchors:
                        if ganchor.name == "markAbove":
                            ganchor.x = x + anchor.x
                            ganchor.y = y + anchor.y
                if anchor.name == 'markAbove_2':
                    for ganchor in glyph.anchors:
                        if ganchor.name == "markAbove_2":
                            ganchor.x = x + anchor.x
                            ganchor.y = y + anchor.y
                if anchor.name == 'markBelow' or anchor.name == 'markBelowDot':
                    if glyph.name in ['uni062C', 'uni062C.fina', 'uni062C.isol', 'uni0686.fina', 'uni0686.isol',
                                      'uni0686']:
                        continue
                    for ganchor in glyph.anchors:
                        if ganchor.name == "markBelow":
                            ganchor.x = x + anchor.x
                            ganchor.y = y + anchor.y
                else:
                    continue

    def sortGlyphs(self):
        self.UFO.lib['public.glyphOrder'].sort()
