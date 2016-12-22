from defcon import Font, Color
from argl import *
mFont = Font("../sources/lots.ufo")
mUnicodes = mFont.unicodeData
data = mFont.getDataForSerialization()

ufo = Font()
ufo.setDataFromSerialization({'info': data['info']})
layersDict = {}
for nl in range(1,9):
    newLayer = ufo.layers.newLayer('background'+str(nl))
    newLayer.color = Color('1,0,0,1')
    layersDict.update({'layer'+str(nl):newLayer})

for glf in RAWN2C:
    layer = 0
    glfSrc = RAWN2C[glf].split(',')
    for g in glfSrc:
        if layer == 10:
            continue
        try:
            gCode = AGL2UV[g]
            mgName = mUnicodes[gCode]
            glyph = mFont[mgName[0]]
            glyph.name = glf
            glyph.unicode = 0
            if layer > 0:
                currentLayer = layersDict['layer'+str(layer)]
                currentLayer.insertGlyph(glyph)
            else:
                ufo.insertGlyph(glyph)
            layer += 1
            print(g + ' found :)' + '  L ' + str(layer))
        except:
            print('         '+g+' not found in font')
for l in ufo.layers:
    print (l.name)
#print(ufo.glyphSet)
ufo.save('xxx.ufo')
