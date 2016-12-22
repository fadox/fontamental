from __future__ import print_function, division, absolute_import
from fontTools.misc.py23 import *

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
#Alef Mamduda
uni0622.isol:FE81
uni0622.fina:FE82
#Alef Hamza
uni0623.isol:FE83
uni0623.fina:FE84
#Waw Hamza
uni0624.isol:FE85
uni0624.fina:FE86
#Alef Maksura
uni0625.isol:FE87
uni0625.fina:FE88
#Alef Maqsura
uni0626.isol:FE89
uni0626.fina:FE8A
uni0626.init:FE8B
uni0626.medi:FE8C
#Alef
uni0627.isol:FE8D
uni0627.fina:FE8E
#Baa
uni0628.isol:FE8F
uni0628.fina:FE90
uni0628.init:FE91
uni0628.medi:FE92
#Taa Marbuta
uni0629.isol:FE93
uni0629.fina:FE94
#Taa
uni062A.isol:FE95
uni062A.fina:FE96
uni062A.init:FE97
uni062A.medi:FE98
#thaa
uni062B.isol:FE99
uni062B.fina:FE9A
uni062B.init:FE9B
uni062B.medi:FE9C
#Jeem
uni062C.isol:FE9D
uni062C.fina:FE9E
uni062C.init:FE9F
uni062C.medi:FEA0
#Hah
uni062D.isol:FEA1
uni062D.fina:FEA2
uni062D.init:FEA3
uni062D.medi:FEA4
#Khah
uni062E.isol:FEA5
uni062E.fina:FEA6
uni062E.init:FEA7
uni062E.medi:FEA8
#Dal
uni062F.isol:FEA9
uni062F.fina:FEAA
#Thal
uni0630.isol:FEAB
uni0630.fina:FEAC
#Raa
uni0631.isol:FEAD
uni0631.fina:FEAE
#Zai
uni0632.isol:FEAF
uni0632.fina:FEB0
#Seen
uni0633.isol:FEB1
uni0633.fina:FEB2
uni0633.init:FEB3
uni0633.medi:FEB4
#Sheen
uni0634.isol:FEB5
uni0634.fina:FEB6
uni0634.init:FEB7
uni0634.medi:FEB8
#Saad
uni0635.isol:FEB9
uni0635.fina:FEBA
uni0635.init:FEBB
uni0635.medi:FEBC
#Daad
uni0636.isol:FEBD
uni0636.fina:FEBE
uni0636.init:FEBF
uni0636.medi:FEC0
#Taah
uni0637.isol:FEC1
uni0637.fina:FEC2
uni0637.init:FEC3
uni0637.medi:FEC4
#Daah
uni0638.isol:FEC5
uni0638.fina:FEC6
uni0638.init:FEC7
uni0638.medi:FEC8
#A'ain
uni0639.isol:FEC9
uni0639.fina:FECA
uni0639.init:FECB
uni0639.medi:FECC
#Ghain
uni063A.isol:FECD
uni063A.fina:FECE
uni063A.init:FECF
uni063A.medi:FED0
#Faa
uni0641.isol:FED1
uni0641.fina:FED2
uni0641.init:FED3
uni0641.medi:FED4
#Qaaf
uni0642.isol:FED5
uni0642.fina:FED6
uni0642.init:FED7
uni0642.medi:FED8
#Kaaf
uni0643.isol:FED9
uni0643.fina:FEDA
uni0643.init:FEDB
uni0643.medi:FEDC
#Laam
uni0644.isol:FEDD
uni0644.fina:FEDE
uni0644.init:FEDF
uni0644.medi:FEE0
#Meem
uni0645.isol:FEE1
uni0645.fina:FEE2
uni0645.init:FEE3
uni0645.medi:FEE4
#Noon
uni0646.isol:FEE5
uni0646.fina:FEE6
uni0646.init:FEE7
uni0646.medi:FEE8
#Heh
uni0647.isol:FEE9
uni0647.fina:FEEA
uni0647.init:FEEB
uni0647.medi:FEEC
#Waw
uni0648.isol:FEED
uni0648.fina:FEEE
#Aleef Maqsuar
uni0649.isol:FEEF
uni0649.fina:FEF0
#Yaa
uni064A.isol:FEF1
uni064A.fina:FEF2
uni064A.init:FEF3
uni064A.medi:FEF4
#Raw Baa
uni066E.isol:E6E0
uni066E.fina:E6E1
uni066E.init:E6E2
uni066E.medi:E6E3
#Raw Qaaf
uni066F.isol:E6F0
uni066F.fina:E6F1
uni066F.init:E6F2
uni066F.medi:E6F3
#Alef Wasla
uni0671.isol:FB50
uni0671.fina:FB51
#Pee
uni067E.isol:FB56
uni067E.fina:FB57
uni067E.init:FB58
uni067E.medi:FB59
#Chee
uni0686.isol:FB7A
uni0686.fina:FB7B
uni0686.init:FB7C
uni0686.medi:FB7D
#Djahl
uni068E.isol:FB86
uni068E.fina:FB87
#Raa V
uni0695.isol:E950
uni0695.fina:E951
#Jhee
uni0698.isol:FB8A
uni0698.fina:FB8B
#Raw Faa
uni06A1.isol:EA10
uni06A1.fina:EA11
uni06A1.init:EA12
uni06A1.medi:EA13
#Vee
uni06A4.isol:FB6A
uni06A4.fina:FB6B
uni06A4.init:FB6C
uni06A4.medi:FB6D
#Keheh
uni06A9.isol:FB8E
uni06A9.fina:FB8F
uni06A9.init:FB90
uni06A9.medi:FB91
#Gaf
uni06AF.isol:FB92
uni06AF.fina:FB93
uni06AF.init:FB94
uni06AF.medi:FB95
#Lamm V
uni06B5.isol:EB50
uni06B5.fina:EB51
uni06B5.init:EB52
uni06B5.medi:EB53
#Raw Noon
uni06BA.isol:FB9E
uni06BA.fina:FB9F
uni06BA.init:EBA2
uni06BA.medi:EBA3
#Noon Ring
uni06BC.isol:EBC0
uni06BC.fina:EBC1
uni06BC.init:EBC2
uni06BC.medi:EBC3
#Heh Doshanbah
uni06BE.isol:FBAA
uni06BE.fina:FBAB
uni06BE.init:FBAC
uni06BE.medi:FBAD
#Heh Hamza
uni06C0.isol:FBA4
uni06C0.fina:FBA5
#Waw V
uni06C6.isol:FBD9
uni06C6.fina:FBDA
#Waw 2 Dot
uni06CA.isol:ECA0
uni06CA.fina:ECA1
#Waw 3 Dot
uni06CB.isol:FBDE
uni06CB.fina:FBDF
#Farsi Yaa
uni06CC.isol:FBFC
uni06CC.fina:FBFD
uni06CC.init:FBFE
uni06CC.medi:FBFF
#Yaa V
uni06CE.isol:ECE0
uni06CE.fina:ECE1
uni06CE.init:ECE2
uni06CE.medi:ECE3
#Yaa Vertical Dots
uni06D0.isol:FBE4
uni06D0.fina:FBE5
uni06D0.init:FBE6
uni06D0.medi:FBE7
#Kurdish Bzwin
uni06D5.isol:ED50
uni06D5.fina:ED51
#Arabic LA
uni06440622.isol:FEF5
uni06440622.fina:FEF6
uni06440623.isol:FEF7
uni06440623.fina:FEF8
uni06440625.isol:FEF9
uni06440625.fina:FEFA
uni06B50627.isol:EF10
uni06B50627.fina:EF11
#Farsi Numbers
uni06F0:06F0
uni06F1:06F1
uni06F2:06F2
uni06F3:06F3
uni06F7:06F7
uni06F8:06F8
uni06F9:06F9
"""


class ARGLError(Exception):
    pass


AGL2UV = {}
UV2AGL = {}


def _builddicts():
    import re

    lines = _arglText.splitlines()

    parseARGL_RE = re.compile("(.*):([A-Za-z_0-9.]+)$")

    for line in lines:
        if not line or line[:1] == '#':
            continue
        m = parseARGL_RE.match(line)
        if not m:
            raise ARGLError("syntax error in glyphlist.txt: %s" % repr(line[:20]))
        unicode = m.group(2)
        assert len(unicode) == 4
        unicode = int(unicode, 16)
        glyphName = m.group(1)
        if glyphName in AGL2UV:
            # the above table contains identical duplicates
            assert AGL2UV[glyphName] == unicode
        else:
            AGL2UV[glyphName] = unicode
        UV2AGL[unicode] = glyphName
_builddicts()


_arglRaw = """\
0627 arAlef.isol uni0627 uni0627,uni0627.isol,uni0623,uni0625,uni0622
062D arHah.isol uni062D uni062D,uni062E,uni062C,uni0686,uni0629,uni06C0,uni06D5
062F arDal.isol uni062F uni062F,uni0630,uni068E
0631 arReh.isol uni0631 uni0630,uni0632,uni0695,uni0698
0633 arSeen.isol uni0633 uni0633,uni0634
0635 arSad.isol uni0635 uni0635,uni0636
0637 arTah.isol uni0637 uni0637,uni0638
0639 arAin.isol uni0639 uni0639,uni063A
0643 arKaf.isol uni0643 uni0643
0644 arLam.isol uni0644 uni0644,uni06B5
0645 arMeem.isol uni0645 uni0645
0647 arHeh.isol uni0647 uni0647
0648 arWaw.isol uni0648 uni0648,uni0624,uni06C6,uni06CA,uni06CB
0649 arYeh.isol uni0649 uni0649,uni064A,uni06CE,uni06D0
065A arSmallV.above uni065A
066E arBeh.isol uni066E uni066E,uni0628,uni062A,uni062B,uni067E
066F arQaf.isol uni066F uni066F,uni0642
06A1 arFeh.isol uni06A1 uni06A1,uni0641,uni06A4
06A9 arKeheh.isol uni06A9 uni06A9,uni06AF
06AF arGaf.isol uni06AF uni06AF
06BA arNoon.isol uni06BA uni06BA,uni0646,uni06BC
06BE arHehDo.isol uni06BE uni06BE

E6E1 arBeh.fina uni066E.fina uni066E.fina,uni0628.fina,uni062A.fina,uni062B.fina,uni067E.fina
E6E2 arBeh.init uni066E.init uni066E.init,uni0628.init,uni062A.init,uni062B.init,uni067E.init
E6E3 arBeh.medi uni066E.medi uni066E.medi,uni0628.medi,uni062A.medi,uni062B.medi,uni067E.medi
E6F1 arQaf.fina uni066F.fina uni066F.fina, uni0642.fina
EA11 arFeh.fina uni06A1.fina uni06A1.fina,uni0641.fina,uni06A4.fina
EA12 arFeh.init uni06A1.init uni06A1.init,uni0641.init,uni06A4.init
EA13 arFeh.medi uni06A1.medi uni06A1.medi,uni0641.medi,uni06A4.medi
EE07 arSad.above uniEE07 uniEE07
EE09 arKaf.above uniEE09 uniEE09
EE0A arHamza.above uniEE0A uniEE0A
EE0B arGaf.above uniEE0B uniEE0B
EE0C arSmallV.below uniEE0C uniEE0C
EE30 arAlefShort.isol uniEE30 uniEE30
EE31 arAlefShort.fina uniEE31 uniEE31
EE50 arFE.isol uniEE50 uniEE50
EE52 arBR.fina uniEE52 uniEE52
EE53 arBN.fina uniEE53 uniEE53
EE54 arBE.isol uniEE54 uniEE54
EE55 arBE.fina uniEE55 uniEE55
EE56 arBM.isol uniEE56 uniEE56
EE57 arBM.init uniEE57 uniEE57
EE58 arBG.init uniEE58uniEE58
FB8F arKeheh.fina uni06A9.fina uni06A9.fina,uni06AF.fina
FB93 arGaf.fina uni06AF.fina uni06AF.fina
FB94 arGaf.init uni06AF.init uni06AF.init
FB95 arGaf.medi uni06AF.medi uni06AF.medi
FB9F arNoon.fina uni06BA.fina uni06BA.fina,uni0646.fina,uni06BC.fina
FBAB arHehDo.fina uni06BE.fina uni06BE.fina

FBB2 ar1Dot.above uniFBB2 uniFBB2,uni0646.init
FBB3 ar1Dot.below uniFBB3 uniFBB3,uni0628.init
FBB4 ar2Dot.above uniFBB4 uniFBB4,uni062A.init
FBB5 ar2Dot.below uniFBB5 uniFBB5,uni064A.init
FBB6 ar3Dot.above uniFBB6 uniFBB6,uni062B.init
FBB9 ar3IDot.below uniFBB9 uniFBB9,uni067E.init
FBBD ar2VDot.above uniFBBD uniFBBD,uni06D0.init
FBBE ar2VDot.below uniFBBE uniFBBE,uni06D0.init
FBBF arRing.below uniFBBF uniFBBF,uni06BC.init

FC40 arLG.isol uniFC40 uniFC40
FC42 arLM.isol uniFC42 uniFC42
FC43 arLE.isol uniFC43 uniFC43
FC80 arSM.init uniFC80 uniFC80
FCAA arGM.init uniFCAA uniFCAA
FCC1 arLG.init uniFCC1 uniFCC1
FCCC arLM.init uniFCCC uniFCCC
FCCF arMG.init uniFCCF uniFCCF
FCD1 arMM.init uniFCD1 uniFCD1
FD88 arLMG.init uniFD88 uniFD88

FE8E arAlef.fina uni0627.fina uni0627.fina,uni0623.fina,uni0625.fina,uni0622.fina
FEA2 arHah.fina uni062D.fina uni062D.fina,uni062E.fina,uni062C.fina,uni0686.fina
FEA3 arHah.init uni062D.init uni062D.init,uni062E.init,uni062C.init,uni0686.init
FEA4 arHah.medi uni062D.medi uni062D.medi,uni062E.medi,uni062C.medi,uni0686.medi
FEAA arDal.fina uni062F.fina uni062F.fina,uni0630.fina,uni068E.fina
FEAE arReh.fina uni0631.fina uni0630.fina,uni0632.fina,uni0695.fina,uni0698.fina
FEB2 arSeen.fina uni0633.fina uni0633.init,uni0634.init
FEB3 arSeen.init uni0633.init uni0633.init,uni0634.init
FEB4 arSeen.medi uni0633.medi uni0633.init,uni0634.init
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
FEE0 arLam.medi uni0644.medi uni0644,uni06B5
FEE2 arMeem.fina uni0645.fina uni0645.fina
FEE3 arMeem.init uni0645.init uni0645.init
FEE4 arMeem.medi uni0645.medi uni0645.medi
FEEA arHeh.fina uni0647.fina uni0647.fina,uni0629.fina,uni06C0.fina,uni06D5.fina
FEEB arHeh.init uni0647.init uni0647.init
FEEC arHeh.medi uni0647.medi uni0647.medi
FEEE arWaw.fina uni0648.fina uni0648.fina,uni0624.fina,uni06C6.fina,uni06CA.fina,uni06CB.fina
FEF0 arYeh.fina uni0649.fina uni0649.fina,uni064A.fina,uni06CE.fina,uni06D0.fina

FEFB arLA.isol uni06440627.isol uni06440627.isol
FEFC arLA.fina uni06440627.fina uni06440627.fina

0621 uni0621 uni0621
0640 uni0640 uni0640
0661 uni0661 uni0661
0660 uni0660 uni0660
064F uni064F uni064F
064E uni064E uni064E
064C uni064C uni064C
064B uni064B uni064B
0654 uni0654 uni0654
0655 uni0655 uni0655
0650 uni0650 uni0650
0667 uni0667 uni0667
0653 uni0653 uni0653
064D uni064D uni064D
060C uni060C uni060C
0663 uni0663 uni0663
0662 uni0662 uni0662
0665 uni0665 uni0665
0664 uni0664 uni0664
0666 uni0666 uni0666
0669 uni0669 uni0669
0668 uni0668 uni0668
0656 uni0656 uni0656
066A uni066A uni066A
066C uni066C uni066C
066B uni066B uni066B
066D uni066D uni066D
0651 uni0651 uni0651
0652 uni0652 uni0652
0670 uni0670 uni0670
06F5 uni06F5 uni06F5
06F4 uni06F4 uni06F4
06F6 uni06F6 uni06F6
061B uni061B uni061B
061F uni061F uni061F
06D4 uni06D4 uni06D4
"""

RAWU2N = {}
RAWN2U = {}
RAWN2G = {}
RAWN2C = {}

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