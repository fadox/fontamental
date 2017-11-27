#!/usr/bin/env python
# encoding: utf-8

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

RAWN2M = {}
"""
Producton Font Glyphs
"""

_arglText = """\
# -----------------------------------------------------------
# Copyright 1997, 2017 Fadox.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or
# without modification, are permitted provided that the
# following conditions are met:
#
# Redistributions of source code must retain the above
# copyright notice, this list of conditions and the following
# disclaimer.
#
# Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following
# disclaimer in the documentation and/or other materials
# provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------
# Name:          Arabic Glyph List For Ali Uni Fonts
# Table version: 1.0
# Date:          December 10, 2016
# URL:           http://fadox.net
#
#END

#Hamza
uni0621 0621 arHamza.isol
uni0621.isol FE80 arHamza.isol

#Alef Mamduda
uni0622 0622 arAlef.isol,diMadda
uni0622.isol FE81 arAlef.isol,diMadda
uni0622.fina FE82 arAlef.fina,diMadda

#Alef Hamza
uni0623 0623 arAlefShort.isol,diHamza.above
uni0623.isol FE83 arAlefShort.isol,diHamza.above
uni0623.fina FE84 arAlefShort.fina,diHamza.above

#Waw Hamza
uni0624 0624 arWaw.isol,diHamza
uni0624.isol FE85 arWaw.isol,diHamza
uni0624.fina FE86 arWaw.fina,diHamza

#Alef Maksura
uni0625 0625 arAlef.isol,diHamza.below
uni0625.isol FE87 arAlef.isol,diHamza.below
uni0625.fina FE88 arAlef.fina,diHamza.below

#Alef Maqsura
uni0626 0626 arYeh.isol,diHamza
uni0626.isol FE89 arYeh.isol,diHamza
uni0626.fina FE8A arYeh.fina,diHamza
uni0626.init FE8B arBeh.init,diHamza
uni0626.medi FE8C arBeh.medi,diHamza

#Alef
uni0627 0627 arAlef.isol
uni0627.isol FE8D arAlef.isol
uni0627.fina FE8E arAlef.fina

#Alef Short
uniEE30 EE30 arAlefShort.isol
uniEE31 EE31 arAlefShort.fina

#Baa
uni0628 0628 arBeh.isol,di1Dot.below
uni0628.isol FE8F arBeh.isol,di1Dot.below
uni0628.fina FE90 arBeh.fina,di1Dot.below
uni0628.init FE91 arBeh.init,di1Dot.below
uni0628.medi FE92 arBeh.medi,di1Dot.below
uniFE91.yeh EE91 arBeh.init.yeh,di1Dot.below

#Taa Marbuta
uni0629 0629 arHeh.isol,di2Dot.above
uni0629.isol FE93 arHeh.isol,di2Dot.above
uni0629.fina FE94 arHeh.fina,di2Dot.above


#Taa
uni062A 062A arBeh.isol,di2Dot.above
uni062A.isol FE95 arBeh.isol,di2Dot.above
uni062A.fina FE96 arBeh.fina,di2Dot.above
uni062A.init FE97 arBeh.init,di2Dot.above
uni062A.medi FE98 arBeh.medi,di2Dot.above


#TTeh
uni0679 0679 arBeh.isol,diTah.above
uni0679.isol FB66 arBeh.isol,diTah.above
uni0679.fina FB67 arBeh.fina,diTah.above
uni0679.init FB68 arBeh.init,diTah.above
uni0679.medi FB69 arBeh.medi,diTah.above


#thaa
uni062B 062B arBeh.isol,di3Dot.above
uni062B.isol FE99 arBeh.isol,di3Dot.above
uni062B.fina FE9A arBeh.fina,di3Dot.above
uni062B.init FE9B arBeh.init,di3Dot.above
uni062B.medi FE9C arBeh.medi,di3Dot.above

#Jeem
uni062C 062C arHah.isol,di1Dot.below
uni062C.isol FE9D arHah.isol,di1Dot.below
uni062C.fina FE9E arHah.fina,di1Dot.below
uni062C.init FE9F arHah.init,di1Dot.below
uni062C.medi FEA0 arHah.medi,di1Dot.below

#Hah
uni062D 062D arHah.isol
uni062D.isol FEA1 arHah.isol
uni062D.fina FEA2 arHah.fina
uni062D.init FEA3 arHah.init
uni062D.medi FEA4 arHah.medi

#Khah
uni062E 062E arHah.isol,di1Dot.above
uni062E.isol FEA5 arHah.isol,di1Dot.above
uni062E.fina FEA6 arHah.fina,di1Dot.above
uni062E.init FEA7 arHah.init,di1Dot.above
uni062E.medi FEA8 arHah.medi,di1Dot.above

#Dal
uni062F 062F arDal.isol
uni062F.isol FEA9 arDal.isol
uni062F.fina FEAA arDal.fina

#DDal
uni0688 0688 arDal.isol,diTah.above
uni0688.isol FB88 arDal.isol,diTah.above
uni0688.fina FB89 arDal.fina,diTah.above

#Thal
uni0630 0630 arDal.isol,di1Dot.above
uni0630.isol FEAB arDal.isol,di1Dot.above
uni0630.fina FEAC arDal.fina,di1Dot.above

#Raa
uni0631 0631 arReh.isol
uni0631.isol FEAD arReh.isol
uni0631.fina FEAE arReh.fina

#RReh
uni0691 0691 arReh.isol,diTah.above
uni0691.isol FB8C arReh.isol,diTah.above
uni0691.fina FB8D arReh.fina,diTah.above

#Zai
uni0632 0632 arReh.isol,di1Dot.above
uni0632.isol FEAF arReh.isol,di1Dot.above
uni0632.fina FEB0 arReh.fina,di1Dot.above

#Seen
uni0633 0633 arSeen.isol
uni0633.isol FEB1 arSeen.isol
uni0633.fina FEB2 arSeen.fina
uni0633.init FEB3 arSeen.init
uni0633.medi FEB4 arSeen.medi

#Sheen
uni0634 0634 arSeen.isol,di3Dot.above
uni0634.isol FEB5 arSeen.isol,di3Dot.above
uni0634.fina FEB6 arSeen.fina,di3Dot.above
uni0634.init FEB7 arSeen.init,di3Dot.above
uni0634.medi FEB8 arSeen.medi,di3Dot.above

#Saad
uni0635 0635 arSad.isol
uni0635.isol FEB9 arSad.isol
uni0635.fina FEBA arSad.fina
uni0635.init FEBB arSad.init
uni0635.medi FEBC arSad.medi

#Daad
uni0636 0636 arSad.isol,di1Dot.above
uni0636.isol FEBD arSad.isol,di1Dot.above
uni0636.fina FEBE arSad.fina,di1Dot.above
uni0636.init FEBF arSad.init,di1Dot.above
uni0636.medi FEC0 arSad.medi,di1Dot.above

#Taah
uni0637 0637 arTah.isol
uni0637.isol FEC1 arTah.isol
uni0637.fina FEC2 arTah.fina
uni0637.init FEC3 arTah.init
uni0637.medi FEC4 arTah.medi

#Daah
uni0638 0638 arTah.isol,di1Dot.above
uni0638.isol FEC5 arTah.isol,di1Dot.above
uni0638.fina FEC6 arTah.fina,di1Dot.above
uni0638.init FEC7 arTah.init,di1Dot.above
uni0638.medi FEC8 arTah.medi,di1Dot.above

#A'ain
uni0639 0639 arAin.isol
uni0639.isol FEC9 arAin.isol
uni0639.fina FECA arAin.fina
uni0639.init FECB arAin.init
uni0639.medi FECC arAin.medi

#Ghain
uni063A 063A arAin.isol,di1Dot.above
uni063A.isol FECD arAin.isol,di1Dot.above
uni063A.fina FECE arAin.fina,di1Dot.above
uni063A.init FECF arAin.init,di1Dot.above
uni063A.medi FED0 arAin.medi,di1Dot.above

#Faa
uni0641 0641 arFeh.isol,di1Dot.above
uni0641.isol FED1 arFeh.isol,di1Dot.above
uni0641.fina FED2 arFeh.fina,di1Dot.above
uni0641.init FED3 arFeh.init,di1Dot.above
uni0641.medi FED4 arFeh.medi,di1Dot.above

#Qaaf
uni0642 0642 arQaf.isol,di2Dot.above
uni0642.isol FED5 arQaf.isol,di2Dot.above
uni0642.fina FED6 arQaf.fina,di2Dot.above
uni0642.init FED7 arFeh.init,di2Dot.above
uni0642.medi FED8 arFeh.medi,di2Dot.above

#Kaaf
uni0643 0643 arKaf.isol
uni0643.isol FED9 arKaf.isol
uni0643.fina FEDA arKaf.fina
uni0643.init FEDB arKaf.init
uni0643.medi FEDC arKaf.medi

#Laam
uni0644 0644 arLam.isol
uni0644.isol FEDD arLam.isol
uni0644.fina FEDE arLam.fina
uni0644.init FEDF arLam.init
uni0644.medi FEE0 arLam.medi

#Meem
uni0645 0645 arMeem.isol
uni0645.isol FEE1 arMeem.isol
uni0645.fina FEE2 arMeem.fina
uni0645.init FEE3 arMeem.init
uni0645.medi FEE4 arMeem.medi

#Noon
uni0646 0646 arNoon.isol,di1Dot.above
uni0646.isol FEE5 arNoon.isol,di1Dot.above
uni0646.fina FEE6 arNoon.fina,di1Dot.above
uni0646.init FEE7 arBeh.init,di1Dot.above
uni0646.medi FEE8 arBeh.medi,di1Dot.above

#Heh
uni0647 0647 arHeh.isol
uni0647.isol FEE9 arHeh.isol
uni0647.fina FEEA arHeh.fina
uni0647.init FEEB arHeh.init
uni0647.medi FEEC arHeh.medi

#Waw
uni0648 0648 arWaw.isol
uni0648.isol FEED arWaw.isol
uni0648.fina FEEE arWaw.fina

#Aleef Maqsuar
uni0649 0649 arYeh.isol
uni0649.isol FEEF arYeh.isol
uni0649.fina FEF0 arYeh.fina

#Yaa
uni064A 064A arYeh.isol,di2Dot.below
uni064A.isol FEF1 arYeh.isol,di2Dot.below
uni064A.fina FEF2 arYeh.fina,di2Dot.below
uni064A.init FEF3 arBeh.init,di2Dot.below
uni064A.medi FEF4 arBeh.medi,di2Dot.below

#Raw Baa
uni066E 066E arBeh.isol
uni066E.isol E6E0 arBeh.isol
uni066E.fina E6E1 arBeh.fina
uni066E.init E6E2 arBeh.init
uni066E.medi E6E3 arBeh.medi
uniFBE8 FBE8 arBeh.init
uniFBE9 FBE9 arBeh.medi

#Raw Qaaf
uni066F 066F arQaf.isol
uni066F.isol E6F0 arQaf.isol
uni066F.fina E6F1 arQaf.fina
uni066F.init E6F2 arFeh.init
uni066F.medi E6F3 arFeh.medi

#Alef Wasla
uni0671 0671 arAlefShort.isol,diWasla
uni0671.isol FB50 arAlefShort.isol,diWasla
uni0671.fina FB51 arAlefShort.fina,diWasla

#Pee
uni067E 067E arBeh.isol,di3IDot.below
uni067E.isol FB56 arBeh.isol,di3IDot.below
uni067E.fina FB57 arBeh.fina,di3IDot.below
uni067E.init FB58 arBeh.init,di3IDot.below
uni067E.medi FB59 arBeh.medi,di3IDot.below

#Chee
uni0686 0686 arHah.isol,di3IDot.below
uni0686.isol FB7A arHah.isol,di3IDot.below
uni0686.fina FB7B arHah.fina,di3IDot.below
uni0686.init FB7C arHah.init,di3IDot.below
uni0686.medi FB7D arHah.medi,di3IDot.below

#Djahl
uni068E 068E arDal.isol,di3Dot.above
uni068E.isol FB86 arDal.isol,di3Dot.above
uni068E.fina FB87 arDal.fina,di3Dot.above

#Raa V
uni0695 0695 arReh.isol,diSmallV.below
uni0695.isol E950 arReh.isol,diSmallV.below
uni0695.fina E951 arReh.fina,diSmallV.below

#Jhee
uni0698 0698 arReh.isol,di3Dot.above
uni0698.isol FB8A arReh.isol,di3Dot.above
uni0698.fina FB8B arReh.fina,di3Dot.above

#Raw Faa
uni06A1 06A1 arFeh.isol
uni06A1.isol EA10 arFeh.isol
uni06A1.fina EA11 arFeh.fina
uni06A1.init EA12 arFeh.init
uni06A1.medi EA13 arFeh.medi

#Vee
uni06A4 06A4 arFeh.isol,di3Dot.above
uni06A4.isol FB6A arFeh.isol,di3Dot.above
uni06A4.fina FB6B arFeh.fina,di3Dot.above
uni06A4.init FB6C arFeh.init,di3Dot.above
uni06A4.medi FB6D arFeh.medi,di3Dot.above

#Keheh
uni06A9 06A9 arKeheh.isol
uni06A9.isol FB8E arKeheh.isol
uni06A9.fina FB8F arKeheh.fina
uni06A9.init FB90 arKaf.init
uni06A9.medi FB91 arKaf.medi

#Gaf
uni06AF 06AF arKeheh.isol,diGaf.above
uni06AF.isol FB92 arKeheh.isol,diGaf.above
uni06AF.fina FB93 arKeheh.fina,diGaf.above
uni06AF.init FB94 arKaf.init,diGaf.above
uni06AF.medi FB95 arKaf.medi,diGaf.above

#Lamm V
uni06B5 06B5 arLam.isol,diSmallV.above
uni06B5.isol EB50 arLam.isol,diSmallV.above
uni06B5.fina EB51 arLam.fina,diSmallV.above
uni06B5.init EB52 arLam.init,diSmallV.above
uni06B5.medi EB53 arLam.medi,diSmallV.above

#Raw Noon
uni06BA 06BA arNoon.isol
uni06BA.isol FB9E arNoon.isol
uni06BA.fina FB9F arNoon.fina
uni06BA.init EBA2 arBeh.init
uni06BA.medi EBA3 arBeh.medi

#Noon Ring
uni06BC 06BC arNoon.isol,di1Dot.above,diRing.below
uni06BC.isol EBC0 arNoon.isol,di1Dot.above,diRing.below
uni06BC.fina EBC1 arNoon.fina,di1Dot.above,diRing.below
uni06BC.init EBC2 arBeh.init,di1Dot.above,diRing.below
uni06BC.medi EBC3 arBeh.medi,di1Dot.above,diRing.below

#Heh Doshanbah
uni06BE 06BE arHehDo.isol
uni06BE.isol FBAA arHehDo.isol
uni06BE.fina FBAB arHehDo.fina
uni06BE.init FBAC arHeh.init
uni06BE.medi FBAD arHeh.medi

#Heh Hamza
uni06C0 06C0 arHeh.isol,diHamza
uni06C0.isol FBA4 arHeh.isol,diHamza
uni06C0.fina FBA5 arHeh.fina,diHamza

#Waw V
uni06C6 06C6 arWaw.isol,diSmallV.above
uni06C6.isol FBD9 arWaw.isol,diSmallV.above
uni06C6.fina FBDA arWaw.fina,diSmallV.above

#Waw 2 Dot
uni06CA 06CA arWaw.isol,di2Dot.above
uni06CA.isol ECA0 arWaw.isol,di2Dot.above
uni06CA.fina ECA1 arWaw.fina,di2Dot.above

#Waw 3 Dot
uni06CB 06CB arWaw.isol,di3Dot.above
uni06CB.isol FBDE arWaw.isol,di3Dot.above
uni06CB.fina FBDF arWaw.fina,di3Dot.above

#Farsi Yaa
uni06CC 06CC arYeh.isol
uni06CC.isol FBFC arYeh.isol
uni06CC.fina FBFD arYeh.fina
uni06CC.init FBFE arBeh.intt,di2Dot.below
uni06CC.medi FBFF arBeh.medi,di2Dot.below

#Yaa V
uni06CE 06CE arYeh.isol,diSmallV.above
uni06CE.isol ECE0 arYeh.isol,diSmallV.above
uni06CE.fina ECE1 arYeh.fina,diSmallV.above
uni06CE.init ECE2 arBeh.init,di2Dot.below,diSmallV.above
uni06CE.medi ECE3 arBeh.medi,di2Dot.below,diSmallV.above

#Yaa Vertical Dots
uni06D0 06D0 arYeh.isol,di2VDot.below
uni06D0.isol FBE4 arYeh.isol,di2VDot.below
uni06D0.fina FBE5 arYeh.fina,di2VDot.below
uni06D0.init FBE6 arBeh.init,di2VDot.below
uni06D0.medi FBE7 arBeh.medi,di2VDot.below

#Kurdish Bzwin
uni06D5 06D5 arHeh.isol
uni06D5.isol ED50 arHeh.isol
uni06D5.fina ED51 arHeh.fina

#Arabic Numbers
uni0660 0660 dig0
uni0661 0661 dig1
uni0662 0662 dig2
uni0663 0663 dig3
uni0664 0664 dig4
uni0665 0665 dig5
uni0666 0666 dig6
uni0667 0667 dig7
uni0668 0668 dig8
uni0669 0669 dig9

#Farsi Numbers
uni06F0 06F0 dig0
uni06F1 06F1 dig1
uni06F2 06F2 dig2
uni06F3 06F3 dig3
uni06F4 06F4 dig4Farsi
uni06F5 06F5 dig5Farsi
uni06F6 06F6 dig6Farsi
uni06F7 06F7 dig7
uni06F8 06F8 dig8
uni06F9 06F9 dig9

#Arabic Lam Alef Legatur
uni06440627.isol FEFB legLA.isol
uni06440627.fina FEFC legLA.fina
uni06440622.isol FEF5 legLAShort.isol,diMadda
uni06440622.fina FEF6 legLAShort.fina,diMadda
uni06440623.isol FEF7 legLAShort.isol,diHamza.above
uni06440623.fina FEF8 legLAShort.fina,diHamza.above
uni06440625.isol FEF9 legLA.isol,diHamza.below
uni06440625.fina FEFA legLA.fina,diHamza.below
uni06B50627.isol EFFB legLA.isol,diSmallV.above
uni06B50627.fina EFFC legLA.fina,diSmallV.above

#
# Arabic Legatures
#

#allah
uniFDF2 FDF2 legAllah
uniFDFA FDFA legSalah


# Punctation
uni0640 0640 arKashida
uni060C 060C arComma
uni061B 061B arSemicolon
uni061F 061F arQuestion
uni066D 066D arAsterisk
uni066A 066A arPercent
uni066C 066C arThousandsep
uni066B 066B arDecimal
uni06D4 06D4 arFullStop
uniFD3E FD3E arOrnateLeft
uniFD3F FD3F arOrnateRight


# Tanqeet
uniFBB2 FBB2 di1Dot.above
uniFBB3 FBB3 di1Dot.below
uniFBB4 FBB4 di2Dot.above
uniFBB5 FBB5 di2Dot.below
uniFBB6 FBB6 di3Dot.above
uniFBB7 FBB7 di3Dot.below
uniFBB8 FBB8 di3IDot.above
uniFBB9 FBB9 di3IDot.below
uniFBBA FBBA di4Dot.above
uniFBBB FBBB di4Dot.below
uniFBBD FBBD di2VDot.above
uniFBBE FBBE di2VDot.below
uniFBBF FBBF di4Dot.below
uni0615 0615 diTah.above


#diacritic
uniEE0B EE0B diGaf.above
uniEE0A EE0A diHamza
uni065A 065A diSmallV.above
uniEE0C EE0C diSmallV.below
uniEE07 EE07 diWasla
uniFBBF FBBF diRing.below
uni064E 064E diFatha
uni0650 0650 diKasra
uni0651 0651 diShadda
uni064B 064B diFathatan
uni064C 064C diDammatan
uni064F 064F diDamma
uni0652 0652 diSukun
uni064D 064D diKasratan
uni0653 0653 diMadda
uni0654 0654 diHamza.above
uni0655 0655 diHamza.below
uni0670 0670 diLonga.above
uni0656 0656 diLonga.below

"""


class ARGLError(Exception):
    pass

def _builddicts():
    for line in _arglText.splitlines():
        if not line or line[:1] == '#':
            continue

        splitRaw = line.split()

        if len(splitRaw) < 2:
            continue

        unicode = splitRaw[1]
        assert len(unicode) == 4
        unicode = int(unicode, 16)
        glyphName = splitRaw[0]
        if glyphName in AGL2UV:
            # the above table contains identical duplicates
            assert AGL2UV[glyphName] == unicode
        else:
            AGL2UV[glyphName] = unicode
            try:
                AGL2FEA[glyphName] = splitRaw[2].split(",")
            except:
                pass
        UV2AGL[unicode] = glyphName
_builddicts()





"""
Master Font Glyphs
"""

_arglRaw = """\
# -----------------------------------------------------------
# Copyright 1997, 2017 Fadox.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or
# without modification, are permitted provided that the
# following conditions are met:
#
# Redistributions of source code must retain the above
# copyright notice, this list of conditions and the following
# disclaimer.
#
# Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following
# disclaimer in the documentation and/or other materials
# provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------
# Name:          Arabic Glyph List For Ali Uni Fonts
# Table version: 1.0
# Date:          December 10, 2016
# URL:           http://fadox.net
#
#END

# Arabic Isol glyphs
0621 arHamza.isol uni0621 uni0621,uni0621.isol
0627 arAlef.isol uni0627 uni0627,uni0627.isol,uni0623,uni0623.isol,uni0625,uni0625.isol,uni0622,uni0622.isol
062D arHah.isol uni062D uni062D,uni062D.isol,uni062E,uni062E.isol,uni062C,uni062C.isol,uni0686,uni0686.isol
062F arDal.isol uni062F uni062F,uni062F.isol,uni0630,uni0630.isol,uni068E,uni068E.isol
0631 arReh.isol uni0631 uni0631,uni0631.isol,uni0632,uni0632.isol,uni0695,uni0695.isol,uni0698,uni0698.isol
0633 arSeen.isol uni0633 uni0633,uni0633.isol,uni0634,uni0634.isol
0635 arSad.isol uni0635 uni0635,uni0635.isol,uni0636,uni0636.isol
0637 arTah.isol uni0637 uni0637,uni0637.isol,uni0638,uni0638.isol
0639 arAin.isol uni0639 uni0639,uni0639.isol,uni063A,uni063A.isol
0643 arKaf.isol uni0643 uni0643,uni0643.isol
0644 arLam.isol uni0644 uni0644,uni0644.isol,uni06B5,uni06B5.isol
0645 arMeem.isol uni0645 uni0645,uni0645.isol
0647 arHeh.isol uni0647 uni0647,uni0647.isol,uni06D5,uni06D5.isol,uni0629,uni0629.isol,uni06C0,uni06C0.isol
0648 arWaw.isol uni0648 uni0648,uni0648.isol,uni0624,uni0624.isol,uni06C6,uni06C6.isol,uni06CA,uni06CA.isol,uni06CB,uni06CB.isol
0649 arYeh.isol uni0649 uni0649,uni0649.isol,uni064A,uni064A.isol,uni06CE,uni06CE.isol,uni06D0,uni06D0.isol
066E arBeh.isol uni066E uni066E,uni066E.isol,uni0628,uni0628.isol,uni062A,uni062A.isol,uni062B,uni062B.isol,uni067E,uni067E.isol
066F arQaf.isol uni066F uni066F,uni066F.isol,uni0642,uni0642.isol
06A1 arFeh.isol uni06A1 uni06A1,uni06A1.isol,uni0641,uni0641.isol,uni06A4,uni06A4.isol
06A9 arKeheh.isol uni06A9 uni06A9,uni06A9.isol,uni06AF,uni06AF.isol
#06AF arGaf.isol uni06AF uni06AF,uni06AF.isol
06BA arNoon.isol uni06BA uni06BA,uni06BA.isol,uni0646,uni0646.isol,uni06BC,uni06BC.isol
06BE arHehDo.isol uni06BE uni06BE,uni06BE.isol
EE30 arAlefShort.isol uniEE30 uniEE30,uni0623,uni0623.isol,uni0622,uni0622.isol


# Arabic Presentations
E6E1 arBeh.fina uni066E.fina uni066E.fina,uni0628.fina,uni062A.fina,uni062B.fina
E6E2 arBeh.init uni066E.init uni066E.init,uni0628.init,uni062A.init,uni062B.init
E6E3 arBeh.medi uni066E.medi uni066E.medi,uni0628.medi,uni062A.medi,uni062B.medi
E6F1 arQaf.fina uni066F.fina uni066F.fina,uni0642.fina
EA11 arFeh.fina uni06A1.fina uni06A1.fina,uni0641.fina,uni06A4.fina
EA12 arFeh.init uni06A1.init uni06A1.init,uni0641.init,uni06A4.init
EA13 arFeh.medi uni06A1.medi uni06A1.medi,uni0641.medi,uni06A4.medi


FB8F arKeheh.fina uni06A9.fina uni06A9.fina,uni06AF.fina

FB9F arNoon.fina uni06BA.fina uni06BA.fina,uni0646.fina,uni06BC.fina
FBAB arHehDo.fina uni06BE.fina uni06BE.fina
FE8E arAlef.fina uni0627.fina uni0627.fina,uni0623.fina,uni0625.fina,uni0622.fina
FEA2 arHah.fina uni062D.fina uni062D.fina,uni062E.fina,uni062C.fina,uni0686.fina
FEA3 arHah.init uni062D.init uni062D.init,uni062E.init,uni062C.init,uni0686.init
FEA4 arHah.medi uni062D.medi uni062D.medi,uni062E.medi,uni062C.medi,uni0686.medi
FEAA arDal.fina uni062F.fina uni062F.fina,uni0630.fina,uni068E.fina
FEAE arReh.fina uni0631.fina uni0631.fina,uni0632.fina,uni0695.fina,uni0698.fina
FEB2 arSeen.fina uni0633.fina uni0633.fina,uni0634.fina
FEB3 arSeen.init uni0633.init uni0633.init,uni0634.init
FEB4 arSeen.medi uni0633.medi uni0633.medi,uni0634.medi
FEBA arSad.fina uni0635.fina uni0635.fina,uni0636.fina
FEBB arSad.init uni0635.init uni0635.init,uni0636.init
FEBC arSad.medi uni0635.medi uni0635.medi,uni0636.medi
FEC2 arTah.fina uni0637.fina uni0637.fina,uni0638.fina
FEC3 arTah.init uni0637.init uni0637.init,uni0638.init
FEC4 arTah.medi uni0637.medi uni0637.medi,uni0638.medi
FECA arAin.fina uni0639.fina uni0639.fina,uni063A.fina
FECB arAin.init uni0639.init uni0639.init,uni063A.init
FECC arAin.medi uni0639.medi uni0639.medi,uni063A.medi
FEDA arKaf.fina uni0643.fina uni0643.fina
FEDB arKaf.init uni0643.init uni0643.init
FEDC arKaf.medi uni0643.medi uni0643.medi
FEDE arLam.fina uni0644.fina uni0644.fina,uni06B5.fina
FEDF arLam.init uni0644.init uni0644.init,uni06B5.init
FEE0 arLam.medi uni0644.medi uni0644.medi,uni06B5.medi
FEE2 arMeem.fina uni0645.fina uni0645.fina
FEE3 arMeem.init uni0645.init uni0645.init
FEE4 arMeem.medi uni0645.medi uni0645.medi
FEEA arHeh.fina uni0647.fina uni0647.fina,uni0629.fina,uni06C0.fina,uni06D5.fina
FEEB arHeh.init uni0647.init uni0647.init
FEEC arHeh.medi uni0647.medi uni0647.medi
FEEE arWaw.fina uni0648.fina uni0648.fina,uni0624.fina,uni06C6.fina,uni06CA.fina,uni06CB.fina
FEF0 arYeh.fina uni0649.fina uni0649.fina,uni064A.fina,uni06CE.fina,uni06D0.fina
EE31 arAlefShort.fina uniEE31 uniEE31,uni0623.fina,uni0622.fina


#Arabic Lam Alef Legatur
FEFB legLA.isol uni06440627.isol uni06440627.isol,uni06440625.isol
FEFC legLA.fina uni06440627.fina uni06440627.fina,uni06440625.fina
FEFD legLAShort.isol uni0644EE31.isol uni0644EE31.isol,uni06440623.isol,uni06440622.isol
FEFE legLAShort.fina uni0644EE31.fina uni0644EE31.fina,uni06440623.fina,uni06440622.fina

#Arabic Legaturess
#EE55 legBE.fina uni066E0649.fina uni066E0649.fina
#FCCF legMG.init uni0645062D.init uni0645062D.init,uni0645062C.init,uni0645062E.init
#FCD1 legMM.init uni06450645.init uni06450645.init
#FD88 legLMG.init uni06440645062D.init uni06440645062D.init
#FC42 legLM.isol uni06440645.isol uni06440645.isol
#FCC1 legLG.init uni0644062D.init uni0644062D.init,uni0644062E.init,uni0644062C.init
#FC40 legLG.isol uni0644062D.isol uni0644062D.isol,uni0644062C.isol,uni0644062E.isol
#FC43 legLE.isol uni06440649.isol uni06440649.isol,uni0644064A.isol
#FC86 legLE.fina uni06440649.fina uni06440649.fina,uni0644064A.fina
#FCAA legGM.init uni062D0645.init uni062D0645.init,uni062E0645.init,uni062C0645.init
#EE54 legBE.isol uni066E0649.isol uni066E0649.isol,uni0628064A.isol,uni062A064A.isol
#EE58 legBG.init uni066E062D.init uni066E062D.init,uni064A062D.init,uni064A062C.init,uni064A062E.init
#EE57 legBM.init uni066E0645.init uni066E0645.init,uni062A0645.init
#EE56 legBM.isol uni066E0645.isol uni066E0645.isol
#EE53 legBN.fina uni066E06BA.fina uni066E06BA.fina,uni064A0646.fina
#EE52 legBR.fina uni066E0631.fina uni066E0631.fina,uni06280631.fina,uni062A0631.fina
#EE50 legFE.isol uni06A10649.isol uni06A10649.isol,uni064A0649.isol
#FC80 legSM.init uni06330645.init uni06330645.init
#FCCC legLM.init uni06440645.init uni06440645.init
FDF2 legAllah uniFDF2 uniFDF2
FDFA legSalah uniFDFA uniFDFA


# Punctation
0640 arKashida uni0640
060C arComma uni060C
061B arSemicolon uni061B
061F arQuestion uni061F
066D arAsterisk uni066D
066A arPercent uni066A
066C arThousandsep uni066C
066B arDecimal uni066B
06D4 arFullStop uni06D4
FD3E arOrnateLeft uniFD3E uniFD3E
FD3F arOrnateRight uniFD3F uniFD3F


#Farsi Numbers
06F4 dig4Farsi uni06F4
06F5 dig5Farsi uni06F5
06F6 dig6Farsi uni06F6

#Arabic Numbers
0660 dig0 uni0660
0661 dig1 uni0661
0662 dig2 uni0662
0663 dig3 uni0663
0664 dig4 uni0664
0665 dig5 uni0665
0666 dig6 uni0666
0667 dig7 uni0667
0668 dig8 uni0668
0669 dig9 uni0669


#diacritic
EE0B diGaf.above uniEE0B uniEE0B,uni06AF.medi
EE0A diHamza uniEE0A uniEE0A,uni0626.medi,uni0624.isol,uni0624.fina
065A diSmallV.above uni065A uni065A,uni06C6,uni06C6.isol
EE0C diSmallV.below uniEE0C uniEE0C,uni0595,uni0595.isol
EE07 diWasla uniEE07 uniEE07,uni0671,uni0671.isol
FBBF diRing.below uniFBBF uniFBBF,uni06BC.init,uni0652
064E diFatha uni064E
0650 diKasra uni0650
0651 diShadda uni0651
064B diFathatan uni064B
064C diDammatan uni064C
064F diDamma uni064F
0652 diSukun uni0652
064D diKasratan uni064D
0653 diMadda uni0653
0654 diHamza.above uni0654
0655 diHamza.below uni0655
0670 diLonga.above uni0670
0656 diLonga.below uni0656

#Tanqeet
FBB2 di1Dot.above uniFBB2 uniFBB2,uni0646.init
FBB3 di1Dot.below uniFBB3 uniFBB3,uni0628.init
FBB4 di2Dot.above uniFBB4 uniFBB4,uni062A.init
FBB5 di2Dot.below uniFBB5 uniFBB5,uni064A.init
FBB6 di3Dot.above uniFBB6 uniFBB6,uni062B.init
FBB7 di3Dot.below uniFBB7
FBB8 di3IDot.above uniFBB8
FBB9 di3IDot.below uniFBB9 uniFBB9,uni067E.init
FBBA di4Dot.above uniFBBA
FBBB di4Dot.below uniFBBB
FBBD di2VDot.above uniFBBD uniFBBD,uni06D0.init
FBBE di2VDot.below uniFBBE uniFBBE,uni06D0.init
0615 diTah.above uni0615
"""


def _buildraws():
    for line in _arglRaw.splitlines():
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


        RAWU2N[uniName] = rawName
        RAWN2U[rawName] = uniName
        RAWN2G[rawName] = splitRaw[2]

        if splitRaw[3] == '#':
            RAWN2C[rawName] = splitRaw[2]
        else:
            RAWN2C[rawName] = splitRaw[3]


_buildraws()
m = 1