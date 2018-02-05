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
import configparser
import io


class GlyphsLib:
    # Arabic Glyphs dict{}, Production glyph name : unicode value
    Prod2Decimal = {}

    # Arabic Glyphs dict{}, unicode value : production glyph name
    Decimal2Prod = {}

    # Arabic Glyphs dict{}, production glyph name : equivalent master glyph names
    Prod2Comp = {}

    # Master Font Glyphs dict{}, unicode hex : master glyph name
    Unicode2Master = {}

    # Master Font Glyphs dict{}, master glyph name : unicode hex
    Master2Unicode = {}

    # Master Font Glyphs dict{}, master glyph name : production glyph name
    Master2Prod = {}

    # Master Font Glyphs dict{}, master glyph name : search sequence
    Master2Search = {}

    # Master Font Glyphs dict{}, master glyph name : mapping
    MAPPING = {}

    # Post modifications
    IRREGULAR = {}

    # Configurations
    CONFIGS = {}

    def __init__(self, buildFea=False, config=None):
        self._init_configs(config)
        self._init_glyphs_database()
        self._create_minify_lists()
        self._create_maxify_lists()
        self._init_irregulars()
        self._init_minify_mapping()

        if buildFea is not False:
            self._build_fea()

    def _init_configs(self, configFile):
        """
        read customized configuration of the font (optional)
        """

        if configFile:
            # Load the configuration file
            config = configparser.RawConfigParser(allow_no_value=True)
            config.optionxform = str
            config.read(configFile, encoding='utf8')

            for section in config.sections():
                if "(dict)" in section:
                    section_name = section.replace('(dict)','')
                    options_dict = {}
                    for options in config.options(section):
                        options_dict[options] = config.get(section, options)
                    self.CONFIGS[section_name] = options_dict
                else:
                    self.CONFIGS[section] = []
                    for options in config.options(section):
                        self._set_config(section, options)


    def _init_glyphs_database(self):
        """
        read fontamental configuration files (all *.txt files) under /database subfolder
        """
        dirPath = os.path.dirname(__file__)
        for filePath in glob(dirPath + os.sep + "database" + os.sep + "*.txt"):
            fp = filePath.split(os.sep)
            fileName = (fp[len(fp) - 1]).split('.')[0]
            text = self._get_file_content(filePath)
            self._set_config_from_text(fileName, text)

    def _get_file_content(self, filePath):
        """
        read the content of given file path, and return the content as a string
        """
        assert os.path.isfile(filePath)
        with codecs.open(filePath, 'r', encoding='utf8') as f:
            lines = f.read()
            return lines

    def _set_config(self, section, option):
        """
        set a Config value, under a given index (name) from a plane text
        """
        linesList = self.CONFIGS[section]
        linesList.append(option)

    def _set_config_from_text(self, name, text):
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
            if rawName in self.Master2Unicode:
                continue
            self.Unicode2Master[uniName] = rawName
            self.Master2Unicode[rawName] = uniName
            self.Master2Prod[rawName] = splitRaw[2]

            if splitRaw[3] == '#':
                self.Master2Search[rawName] = splitRaw[2]
            else:
                self.Master2Search[rawName] = splitRaw[3]

    def _create_maxify_lists(self):
        """
        Create main Configuration Tables to maxify a mini/master font
        """
        assert (self._config_exists('arabic-max'))
        ignored = self._get_config('ignored')
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

            if glyphName in self.Prod2Decimal:
                # the above table contains identical duplicates
                assert self.Prod2Decimal[glyphName] == unicode
            else:
                self.Prod2Decimal[glyphName] = unicode
                try:
                    self.Prod2Comp[glyphName] = splitRaw[2].split(",")
                except Exception:
                    sys.exc_clear()
            self.Decimal2Prod[unicode] = glyphName

    def _init_irregulars(self):
        """
        Applay irregular modifications on glyphs

        This will defined the fine changes that will be applied on the given glyph component
        like changing the position and the component scale
        """
        if not self._config_exists('irregular'):
            return
        transfer_props = ["xScale","yScale", "xOffset", "yOffset"]

        for line in self._get_config('irregular'):
            if "#" in line:
                line = line.split('#')[0]
            if not line:
                continue
            splitMod = line.split()
            if len(splitMod) < 3:
                continue
            gName = splitMod[0]
            cName = splitMod[1]
            cName = self.Master2Prod[cName]
            props = {}
            properties = splitMod[2].split(',')
            for index, p in list(enumerate(properties)):
                props[transfer_props[index]] = p
            self.IRREGULAR[gName] = {cName: props}

    def _init_minify_mapping(self):
        """
        Use a minify mapping

        This function will set the alternative mapping to extract glyphs from base Font
        The mapping values will set to the MAPPING (Name to mapping) global variable
        """
        if not self._config_exists('mapping'):
            return

        for line in self._get_config('mapping'):
            try:
                lp = line.split()
                rawName = lp[0]
                mapping_name = lp[1]
                self.gl.MAPPING[rawName] = mapping_name
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
