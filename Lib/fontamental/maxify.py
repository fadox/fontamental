#!/usr/bin/env python
# encoding: utf-8

from defcon import Font, Color, Glyph, Contour
from fontamental.objects.glyphslib import GlyphsLib
from booleanOperations import BooleanOperationManager
from ufo2ft import compileOTF
import copy
import argparse
import os

class MaxifyUFO():

    def __init__(self, source, config=None):
        self.sourcesDir =os.sep.join(source.split(os.sep)[:-1])
        self.GDB = GlyphsLib(True, config)
        self.srcUFO = Font(source)
        self.UFO = Font()
        self.transFields = ["xScale", "xyScale", "yxScale", "yScale", "xOffset", "yOffset"]

    def build(self):
        self.copyFontInfo()
        self.createGlyphs()
        self.removeOverlap()
        self.setFeatures()
        self.sortGlyphs()
        return self.UFO

    def copyFontInfo(self):
        data = self.srcUFO.getDataForSerialization()
        self.UFO.setDataFromSerialization({'info': data['info']})

    def setFeatures(self):
        featuresText = self.GDB.fea.fea_main
        userFeaFile = self.sourcesDir + os.sep + "font.fea"
        if os.path.isfile(userFeaFile):
            featuresText += self.GDB.get_file_content(userFeaFile)
        self.UFO.features.text = featuresText

    def removeOverlap(self):
        """Removes overlap by combining overlapping contours. Not really necessary,
        but some font rendering systems need this."""
        manager = BooleanOperationManager()
        for glyph in self.UFO:
            contours = list(glyph)
            glyph.clearContours()
            try:
                manager.union(contours, glyph.getPointPen())
            except:
                m = 1

    def createGlyphs(self):

        self.copyFundamentals()
        self.createWhiteSpacesGlyphs()

        subs = self.getSubsets()

        for gName, pgNames in subs.items():
            gModz = {}
            if gName == 'uni062B.medi.yeh':
                m = 1

            if gName in self.GDB.IRREGULAR.keys():
                gModz = self.GDB.IRREGULAR[gName]
            try:
                baseGlyph = self.UFO[pgNames[0]]
                masterGlyph = self.srcUFO[pgNames[0]]

                if not gName in self.UFO.keys():
                    glyph = self.addGlyph(gName, baseGlyph)

                if len(pgNames) == 1:
                    pass
                else:
                    for partName in pgNames[1:]:
                        pModz = []
                        if partName in gModz.keys():
                            pModz = gModz[partName]
                        partGlyph = self.UFO[partName]
                        masterPartGlyph = self.srcUFO[partName]

                        # add parts like Dot, small V, Hamza on the Base Glyph
                        partAnchors = [a.name.replace("_", "", 1) for a in masterPartGlyph.anchors if
                                       a.name.startswith("_")]
                        baseAnchors = [a.name for a in masterGlyph.anchors if not a.name.startswith("_")]

                        anchorName = set(baseAnchors).intersection(partAnchors)
                        assert len(anchorName) > 0, (pgNames[0], partName, partAnchors, baseAnchors)
                        anchorName = list(anchorName)[0]
                        partAnchor = [a for a in masterPartGlyph.anchors if a.name == "_" + anchorName][0]
                        baseAnchor = [a for a in masterGlyph.anchors if a.name == anchorName][0]
                        xoff = baseAnchor.x - partAnchor.x
                        yoff = baseAnchor.y - partAnchor.y
                        self.addComponent(glyph, partName, xoff, yoff, pModz)
                        self.updateAnchors(glyph, masterPartGlyph, xoff, yoff)

                        del baseAnchor, baseAnchors, a, xoff, yoff, partGlyph, anchorName, partName

            except:
                pass

    def getSubsets(self):
        subs = {}
        for gName, pgNames in self.GDB.Prod2Comp.items():
            rep = []
            for el in pgNames:
                rep.append(self.getUniName(el))
            subs[gName] = rep
        return subs

    def getUniName(self, name):
        if name in self.GDB.Master2Prod:
            return self.GDB.Master2Prod[name]
        else:
            return name

    def addGlyph(self, gName, baseGlyph):
        glyph = self.UFO.newGlyph(gName)
        if gName in self.GDB.Prod2Decimal:
            glyph.unicode = self.GDB.Prod2Decimal[gName]
        glyph.width = baseGlyph.width
        glyph.leftMargin = baseGlyph.leftMargin
        glyph.rightMargin = baseGlyph.rightMargin
        self.addComponent(glyph, baseGlyph.name)
        self.addAnchors(glyph, baseGlyph)
        return glyph

    def copyFundamentals(self):
        for g in self.srcUFO:
            if g.name in self.GDB.Master2Unicode:
                gName = self.GDB.Master2Prod[g.name]
                if gName == "uni0646.iso":
                    m = 1
                # print(gName)
                gUnicode = int(self.GDB.Master2Unicode[g.name], 16)
                g.name = gName
                g.unicode = gUnicode
                ng = copy.deepcopy(g)
                self.addAnchors(ng, g)
                self.UFO.insertGlyph(ng)

    def createWhiteSpacesGlyphs(self):
        spaceGlyph = self.UFO['space']
        try:
            spaceWidth = self.GDB.CONFIGS['info']['spaceWidth']
            spaceGlyph.width = int(spaceWidth)
        except:
            print('missing spaceWidth config value')

        space = spaceGlyph.width
        em = self.UFO.info.unitsPerEm

        # no-Break-space 0x00A0
        width = int(space / 2)
        self.createSpaceGlyphe(spaceGlyph, 'nbsp', '00A0', width)

        # en space
        width = int(em / 2)
        self.createSpaceGlyphe(spaceGlyph, 'enspace', '2002', width)

        # em space
        self.createSpaceGlyphe(spaceGlyph, 'emspace', '2003', em)

        # thinspace 0x2009
        width = int(space / 5)
        self.createSpaceGlyphe(spaceGlyph, 'thinspace', '2009', width)

        # hairspace 0x200A
        width = int(space / 7)
        self.createSpaceGlyphe(spaceGlyph, 'hairspace', '200A', width)

        # ZERO WIDTH SPACE 200B
        width = int(space / 7)
        self.createSpaceGlyphe(spaceGlyph, 'hairspace', '200B', 0)

        # ZWNJ 200C
        self.createSpaceGlyphe(spaceGlyph, 'zwnj', '200C', 0)

        # ZWJ 200D
        self.createSpaceGlyphe(spaceGlyph, 'zwj', '200D', 0)

        # lrm  200E
        self.createSpaceGlyphe(spaceGlyph, 'lrm', '200E', 0)

        # rlm 200F
        self.createSpaceGlyphe(spaceGlyph, 'rlm', '200F', 0)

        # ZERO WIDTH NO-BREAK SPACE FEFF
        width = int(space / 7)
        self.createSpaceGlyphe(spaceGlyph, 'zwnbsp', 'FEFF', 0)




        m= 1
    def createSpaceGlyphe(self, spGlyph, name, unicode, width):
        glyph = copy.deepcopy(spGlyph)
        glyph.width = int(width)
        glyph.name = name
        glyph.unicodes = tuple()
        glyph.unicode = int(unicode, 16)
        self.UFO.insertGlyph(glyph)

    def addComponent(self, glyph, name, xoff=0, yoff=0, pModz=[]):
        component = glyph.instantiateComponent()
        component.baseGlyph = name
        component.move((xoff, yoff))
        if len(pModz) > 0:
            trans = component.transformation
            dicts = [dict(zip(self.transFields, d)) for d in [trans]]
            ct = dicts[0]
            for prop in pModz:
                if prop in ("xOffset", "yOffset"):
                    ct[prop] += float(pModz[prop])
                else:
                    ct[prop] = float(pModz[prop])
            newProps = []
            for pn in self.transFields:
                newProps.append(ct[pn])
                component.transformation = tuple(newProps)
        glyph.appendComponent(component)

    def addAnchors(self, glyph, base):
        anchors = base.anchors
        glyph.clearAnchors()
        if glyph.name == 'uniE272':
            m = 1
        markAnchors = ['markAbove', 'markBelow', 'markAbove_1', 'markAbove_2',
                       'markBelow_1', 'markBelow_2', '_markAbove', '_markBelow',
                       '_markAbove_1', '_markAbove_2', '_markBelow_1', '_markBelow_2',
                       '_hamzaAbove', 'hamzaAbove', '_hamzaBelow', 'hamzaBelow'
                       # 'markAboveMark','markBelowMark','_markAboveMark','_markBelowMark'
                       ]
        if len(anchors):
            for anchor in anchors:
                if anchor.name in markAnchors:
                    anc = glyph.instantiateAnchor()
                    anc.x = anchor.x
                    anc.y = anchor.y
                    anc.name = anchor.name
                    glyph.appendAnchor(anc)

                    c = Contour()
                    c.addPoint((anchor.x, anchor.y), name=anchor.name, segmentType="move")
                    glyph.appendContour(c)

                else:
                    continue

    def updateAnchors(self, glyph, base, x, y):
        anchors = base.anchors
        if glyph.name == 'shaddaKasra':
            m = 1
        if len(anchors):
            for anchor in anchors:
                if anchor.name == 'markAbove' or anchor.name == 'markAboveDot' or anchor.name == 'markAboveMark':
                    for ganchor in glyph.anchors:
                        if ganchor.name == "markAbove":
                            ganchor.x = x + anchor.x
                            ganchor.y = y + anchor.y
                if anchor.name == 'markAbove_2':
                    for ganchor in glyph.anchors:
                        if ganchor.name == "markAbove_2":
                            ganchor.x = x + anchor.x
                            ganchor.y = y + anchor.y
                if anchor.name == 'markBelow' or anchor.name == 'markBelowDot' or anchor.name == 'markBelowMark':
                    if glyph.name in ['uni062C', 'uni062C.fina', 'uni062C.isol', 'uni0686.fina', 'uni0686.isol',
                                      'uni0686']:
                        continue
                    for ganchor in glyph.anchors:
                        if ganchor.name == "markBelow":
                            ganchor.x = x + anchor.x
                            ganchor.y = y + anchor.y
                # shadda with kasra or kasratan, will move above 
                if anchor.name == '_markAboveAlt':
                    for ganchor in glyph.anchors:
                        if ganchor.name == "_markAbove":
                            ganchor.x = x + anchor.x
                            ganchor.y = y + anchor.y
                else:
                    continue

    def sortGlyphs(self):
        self.UFO.lib['public.glyphOrder'].sort()


def main():
    config = "./config.ini"
    output = "./build_font.otf"
    parser = argparse.ArgumentParser(prog='maxify')
    parser.add_argument('source', metavar='"Source Font"', type=str,  help='Source File, only UFO format supported')
    parser.add_argument('-c', nargs='?', help='user configuration file path')
    parser.add_argument('-o', nargs='?', help='output file')
    args = parser.parse_args()
    if args.o is not None:
        output = args.o
    source_file = args.source
    if args.c is not None:
        config = args.c
    maxi = MaxifyUFO(source_file, config)
    ufo = maxi.build()
    if ufo is not None:
        otf = compileOTF(ufo, useProductionNames=False)
        if otf is not None:
            # save generated font to file
            otf.save(output)
            print("The Font (" + output + ") created successfully !")

if __name__ == "__main__":
    main()
