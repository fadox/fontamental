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
import sys
from glob import glob
from fontamental.feabuilder import FeaBuilder
import codecs


class GlyphsLib:
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

    # Post modifications
    MODZ = {}

    CONFIGS = {}

    def __init__(self, buildFea=False, config=None):
        self._init_configs(config)
        self._init_lists()
        self._create_minify_lists()
        self._create_maxify_lists()
        self._applay_modifications()
        self._applay_minify_mask()

        if buildFea is not False:
            self._build_fea()

    def _init_configs(self, config):
        """
        read customized configuration of the font (optional)
        """
        if config:
            lines = self._get_file_content(config)
            ns = {}
            code = compile(lines, '<string>', 'exec')
            exec (code, ns)
            cnf = ns['configs']
            if isinstance(cnf, dict):
                for name, text in cnf.items():
                    self._set_config(name, text)

    def _init_lists(self):
        """
        read fontamental configuration files (all *.txt files) under /lists subfolder
        """
        dirPath = os.path.dirname(__file__)
        for filePath in glob(dirPath + os.sep + "lists" + os.sep + "*.txt"):
            fp = filePath.split(os.sep)
            fileName = (fp[len(fp) - 1]).split('.')[0]
            text = self._get_file_content(filePath)
            self._set_config(fileName, text)

    def _get_file_content(self, filePath):
        """
        read the content of given file path, and return the content as a string
        """
        assert os.path.isfile(filePath)
        with codecs.open(filePath, 'r', encoding='utf8') as f:
            lines = f.read()
            return lines

    def _set_config(self, name, text):
        """
        set a Config value, under a given index (name) from a plane text
        """
        linesList = self.CONFIGS[name] = []
        splitRaw = text.split("\n")
        for line in splitRaw:
            line = line.strip(' \t\n\r')
            if not line or line[:1] == '#':
                continue
            linesList.append(line)

    def _get_config(self, index):
        """
        return the dict value of an index in Config dict.
        will return an empty list if the index is not exist or is empty
        """
        if index in self.CONFIGS.keys():
            if isinstance(self.CONFIGS[index], list):
                if len(self.CONFIGS[index]) > 0:
                    return self.CONFIGS[index]
        return []

    def _config_exists(self, index):
        """
        check if an index in exist in Config dict.
        will return True if the index is exists or the value is not an empty list
        """
        if index in self.CONFIGS.keys():
            if isinstance(self.CONFIGS[index], list):
                if len(self.CONFIGS[index]) > 0:
                    return True
        return False

    def _create_minify_lists(self):
        """
        Create main Configuration Tables to minify an original base font to mini/master font
        """
        assert (self._config_exists('arabic-mini'))
        lines = self._get_config('arabic-mini-ext') + self._get_config('arabic-mini')
        for line in lines:
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

    def _create_maxify_lists(self):
        """
        Create main Configuration Tables to maxify a mini/master font
        """
        assert (self._config_exists('arabic-max'))
        ignored = self._get_config('ignore')
        lines = self._get_config('arabic-max-ext') + self._get_config('arabic-max')
        for line in lines:
            splitRaw = line.split()

            if len(splitRaw) < 2:
                continue
            unicode = splitRaw[1]

            assert len(unicode) == 4

            unicode = int(unicode, 16)
            glyphName = splitRaw[0]

            if glyphName in ignored:
                continue

            if glyphName in self.AGL2UV:
                # the above table contains identical duplicates
                assert self.AGL2UV[glyphName] == unicode
            else:
                self.AGL2UV[glyphName] = unicode
                try:
                    self.AGL2FEA[glyphName] = splitRaw[2].split(",")
                except Exception:
                    sys.exc_clear()
            self.UV2AGL[unicode] = glyphName

    def _applay_modifications(self):
        """
        Applay post modifications on glyphs

        This will defined the fine changes that will be applied on the given glyph component
        like changing the position and the component scale
        """
        if not self._config_exists('mod'):
            return

        for line in self._get_config('mod'):
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
            self.MODZ[gName] = {cName: props}

    def _applay_minify_mask(self):
        """
        Use a minify Mask

        This function will set the alternative mapping to extract glyphs from base Font
        The Mask values will set to the RAWN2M (Name to Mask) global variable
        """
        if not self._config_exists('mask'):
            return

        for line in self._get_config('mask'):
            try:
                lp = line.split()
                rawName = lp[0]
                maskName = lp[1]
                self.gl.RAWN2M[rawName] = maskName
            except Exception:
                sys.exc_clear()

    def _build_fea(self):
        """
        Setter: Create the OTF Features Tables for current font

        """
        self.fea = FeaBuilder(self)

    def get_fea(self):
        """
        Getter: return the content of the OTF Features Tables

        """
        return self.fea
