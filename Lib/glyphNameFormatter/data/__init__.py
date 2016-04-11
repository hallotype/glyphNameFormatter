import os
from xml.etree import cElementTree as ET

__slots__ = [
    "unicode2name_AGD",
    "name2unicode_AGD",
    "unicode2name_GLYPHS",
    "name2unicode_GLYPHS",
    "unicodelist",
    "unicodeVersion",
    "unicodeRangeNames",
    ]

path = os.path.dirname(__file__)

# =======
# = AGD =
# =======

unicode2name_AGD = {}
name2unicode_AGD = {}

f = open(os.path.join(path, "AGD.txt"), "r")
lines = f.readlines()
f.close()

# format
# <glyphName>
# <tab> <tag>: <value>

currentGlyphName = None
for line in lines:
    if line.startswith("\t") and currentGlyphName is not None:
        tag, value = line.split(":")
        tag = tag.strip()
        value = value.strip()
        if tag == "uni":
            value = int(value, 16)
            unicode2name_AGD[value] = currentGlyphName
            name2unicode_AGD[currentGlyphName] = value
    else:
        currentGlyphName = line.strip()


# ==========================
# = GLYPHS glyph name list =
# ==========================

# data taken from https://github.com/schriftgestalt/GlyphsInfo/blob/master/GlyphData.xml

unicode2name_GLYPHS = {}
name2unicode_GLYPHS = {}

tree = ET.parse(os.path.join(path, "GlyphData.xml"))

for i in tree.iter():
    if i.tag == "glyph":
        u = i.attrib.get("unicode")
        if u:
            u = int(u, 16)
            n = i.attrib.get("name")
            n = n.split("-")[0]
            unicode2name_GLYPHS[u] = n
            name2unicode_GLYPHS[n] = u

# ================
# = unicode list =
# ================

unicodelist = {}

f = open(os.path.join(path, "flatUnicode.txt"))
lines = f.readlines()
f.close()

unicodeVersion = lines[0].replace("#", "").strip()

for line in lines:
    if line.startswith("#"):
        # a comment
        continue
    line = line.strip()
    if not line:
        # empty line
        continue
    uniNumber, uniName = line.split("\t")
    uniNumber = int(uniNumber, 16)
    unicodelist[uniNumber] = uniName

unicodeVersion = lines[0].replace("#", "").strip()

# ==================
# = unicode blocks =
# ==================

unicodeRangeNames = {}

f = open(os.path.join(path, "unicodeBlocks.txt"))
lines = f.readlines()
f.close()

# format
# Start Code..End Code; Block Name
for line in lines:
    if line.startswith("#"):
        # a comment
        continue
    line = line.strip()
    if not line:
        # empty line
        continue
    rangeValues, rangeName = line.split(";")
    rangeName = rangeName.strip()
    start, end = rangeValues.split("..")
    start = int(start, 16)
    end = int(end, 16)

    unicodeRangeNames[(start, end)] = rangeName
