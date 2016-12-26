from defcon import Font, Color, Glyph
from argl import *
import shutil
import copy


path = "../../ali-uni/build/UFO/Ali-Uni_Samik_Regular.ufo"
path = "../sources/lots.ufo"
#path = "../sources/adobe.ufo"
mFont = Font(path)
mUnicodes = mFont.unicodeData
data = mFont.getDataForSerialization()
master = Font('../sources/font.ufo')
ufo = Font()
ufo.setDataFromSerialization({'info': data['info']})
layersDict = {}
layersColors = ('','1,0,0,1', '0,1,0,1', '0,0,1,1', '0.5,0.5,0,1', '0.5,0,0.5,1', '0,0.5,0.5,1', '0.5,0.5,0.5,1', '1,0,0,1', '1,0,0,1',
'1,0,0,1')
for nl in range(1, 9):
    newLayer = ufo.layers.newLayer('background' + str(nl - 1))
    newLayer.color = Color(layersColors[nl])
    layersDict.update({'layer' + str(nl): newLayer})
ufo.newGlyph('.notdef')

for glf in RAWN2C:
    layer = 0
    glfSrc = RAWN2C[glf].split(',')
    if glf == "legLG.isol":
        m = 1
    for g in glfSrc:
        if layer == 10:
            continue
        try:
            gCode = AGL2UV[g]
            mgName = mUnicodes[gCode]
            glyph = Glyph()
            glyph.copyDataFromGlyph(mFont[mgName[0]])
            glyph.name = glf
            glyph.unicode = None
            glyph.anchors = []
            glyph.decomposeAllComponents()
            if layer > 0:
                currentLayer = layersDict['layer' + str(layer)]
                currentLayer.insertGlyph(glyph)
            else:
                ufo.insertGlyph(glyph)
            layer += 1
            print(g + ' found :)' + '  L ' + str(layer))
        except:
            print('         ' + g + ' not found in font')
        glyph = None
    if layer == 0:
        ufo.newGlyph(glf)
factor = 2
for gg in ufo:
    try:
        masterGlyphe = master[gg.name]
        gg.anchors = copy.deepcopy(masterGlyphe.anchors)
        for point in gg.anchors:
            point.x *= factor
            point.y *= factor
    except:
        pass

def sortLibGlyphs(ufo, type):
    notSorted = ufo.lib['public.glyphOrder']
    sorted = notSorted.sort()
    return sorted


# print(ufo.glyphSet)

sortLibGlyphs(ufo, 'unicode')
outputFilePath = '../sources/build/xxxAA.ufo'
outputFilePath = '../sources/build/xxx888.ufo'
try:
    shutil.rmtree(outputFilePath)
    print(outputFilePath + " Deleted!")
except:
    pass
ufo.save(outputFilePath)
