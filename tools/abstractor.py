from defcon import Font
from argl import *
mFont = Font("../sources/lots.ufo")
mUnicodes = mFont.unicodeData
data = mFont.getDataForSerialization()

ufo = Font()
ufo.setDataFromSerialization({'info': data['info']})
ufo.layers.newLayer('L1')

for glf in RAWN2C:
    layer = 0
    glfSrc = RAWN2C[glf].split(',')
    for g in glfSrc:
        if layer == 2:
            continue
        try:
            gCode = AGL2UV[g]
            mgName = mUnicodes[gCode]
            glyph = mFont[mgName[0]]
            glyph.name = glf
            glyph.unicode = 0
            if layer > 0:
                glyph.lib._set_layer('L1')
            ufo.insertGlyph(glyph)
            layer += 1
            print(g + ' found :)' + '  L ' + str(layer))
        except:
            print('         '+g+' not found in font')
for l in ufo.layers:
    print l.name
#print(ufo.layers)
ufo.save('xxx.ufo')