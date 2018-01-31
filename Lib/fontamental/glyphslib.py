#!/usr/bin/env python
# encoding: utf-8
"""
-----------------------------------------------------------
Copyright 1997, 2017 Fadox.
All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, are permitted provided that the
following conditions are met:

Redistributions of source code must retain the above
copyright notice, this list of conditions and the following
disclaimer.

Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following
disclaimer in the documentation and/or other materials
provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
-----------------------------------------------------------
Name:          Arabic Glyph List For Ali Uni Fonts
Table version: 1.0
Date:          December 10, 2016
last update:   December 16, 2017
URL:           http://fadox.net

END
"""
import os
from glob import glob
from fontamental.feabuilder import FeaBuilder
import codecs


class GlyphsLib():
    """
    AGL  = Production glyph name
    UV   = Production glyph Unicode Value (decimal)
    FEA  = Glyph Component List, with Master glyph Names
    U    = Master glyph equivalent Production Unicode Value (hex)
    RAWU = Master glyph equivalent Production Unicode Value (hex)
    G    = Master glyph equivalent Production glyph name
    RAWN = Master glyph Name
    C    = Aliases of Master glyph in base font, comma seperated Base glyph names
"""
    # Arabic Glyphs dict{}, Production glyph name : unicode value
    AGL2UV = {}

    # Arabic Glyphs dict{}, unicode value : production glyph name
    UV2AGL = {}

    # Arabic Glyphs dict{}, production glyph name : equivalent master glyph names
    AGL2FEA = {}

    # Master Font Glyphs dict{}, unicode hex : master glyph name
    RAWU2N = {}

    # Master Font Glyphs dict{}, master glyph name : unicode hex
    RAWN2U = {}

    # Master Font Glyphs dict{}, master glyph name : production glyph name
    RAWN2G = {}

    # Master Font Glyphs dict{}, master glyph name : search sequence
    RAWN2C = {}

    # Master Font Glyphs dict{}, master glyph name : mask
    RAWN2M = {}

    MODZ = {}

    TEXTLISTS = {}

    def __init__(self, buildFea=False, roles=None):
        self._generateLists()
        if roles:
            self._generateRoles(roles)
        self._createMinifyLists()
        self._createMaxifyLists()

        if self.TEXTLISTS['mod'] is not None:
            self._createModes()

        if buildFea is not False:
            self._buildFea()

    def _generateRoles(self, rolesPath):
        assert os.path.isfile(rolesPath)

        with codecs.open(rolesPath, 'r', encoding='utf8') as f:
            lines = f.read()
            ns = {}
            code = compile(lines, '<string>', 'exec')
            exec(code, ns)
            allRules = ns['roles']
            if isinstance(allRules, dict):
                for name, text in allRules.items():
                    self._readText(name, text)

    def _createModes(self):
        assert len(self.TEXTLISTS['mod']) > 1
        for line in self.TEXTLISTS['mod']:
            if "#" in line:
                line = line.split('#')[0]
            if not line:
                continue
            splitMod = line.split()
            if len(splitMod) < 3:
                continue
            gName = splitMod[0]
            cName = splitMod[1]
            cName = self.RAWN2G[cName]
            props = {}
            properties = splitMod[2].split(';')
            for p in properties:
                splitP = p.split('=')
                props[splitP[0]] = splitP[1]
            self.MODZ[gName] = {cName:props}

    def _createMaxifyLists(self):
        assert len(self.TEXTLISTS['arabic-max']) > 1
        if 'arabic-max-ext' in self.TEXTLISTS:
            self.TEXTLISTS['arabic-max'] = self.TEXTLISTS['arabic-max-ext'] + self.TEXTLISTS['arabic-max']
        for line in self.TEXTLISTS['arabic-max']:
            splitRaw = line.split()

            if len(splitRaw) < 2:
                continue
            unicode = splitRaw[1]
            assert len(unicode) == 4
            unicode = int(unicode, 16)
            glyphName = splitRaw[0]
            if self.TEXTLISTS['ignore'] is not None:
                if glyphName in self.TEXTLISTS['ignore']:
                    continue
            if glyphName in self.AGL2UV:
                # the above table contains identical duplicates
                assert self.AGL2UV[glyphName] == unicode
            else:
                self.AGL2UV[glyphName] = unicode
                try:
                    self.AGL2FEA[glyphName] = splitRaw[2].split(",")
                except:
                    continue
            self.UV2AGL[unicode] = glyphName


    def _createMinifyLists(self):
        assert len(self.TEXTLISTS['arabic-mini']) > 1
        if 'arabic-mini-ext' in self.TEXTLISTS:
            self.TEXTLISTS['arabic-mini'] = self.TEXTLISTS['arabic-mini-ext'] + self.TEXTLISTS['arabic-mini']
        for line in self.TEXTLISTS['arabic-mini']:
            if "#" in line:
                line = line.split('#')[0]
            if not line:
                continue
            line += ' #'
            splitRaw = line.split()

            if len(splitRaw) < 2:
                continue
            uniName = splitRaw[0]
            rawName = splitRaw[1]
            if rawName in self.RAWN2U:
                continue
            self.RAWU2N[uniName] = rawName
            self.RAWN2U[rawName] = uniName
            self.RAWN2G[rawName] = splitRaw[2]

            if splitRaw[3] == '#':
                self.RAWN2C[rawName] = splitRaw[2]
            else:
                self.RAWN2C[rawName] = splitRaw[3]

    def _generateLists(self):
        # read all *.txt files in ./lists
        filePath = os.path.dirname(__file__)
        for txtFile in glob(filePath + os.sep + "lists" + os.sep + "*.txt"):
            fp = txtFile.split(os.sep)
            fileName = (fp[len(fp) - 1]).split('.')[0]
            self._readTextFile(fileName, txtFile)

    def _readText(self, name, text):

        linesList = self.TEXTLISTS[name] = []

        splitRaw = text.split("\n")
        for line in splitRaw:
            line = line.strip(' \t\n\r')
            if not line or line[:1] == '#':
                continue
            linesList.append(line)

    def _readTextFile(self, fileName, filePath):

        assert os.path.isfile(filePath)

        with codecs.open(filePath, 'r', encoding='utf8') as f:
            linesList = self.TEXTLISTS[fileName] = []
            lines = f.read()
            splitRaw = lines.split("\n")
            for line in splitRaw:
                if not line or line[:1] == '#':
                    continue
                linesList.append(line)

    def _buildFea(self):
        self.fea = FeaBuilder(self)

    def getFea(self):
        return self.fea