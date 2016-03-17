
def process(self):
    self.edit("GREEK PROSGEGRAMMENI", "iotaadscript")
    self.processAs("Greek and Coptic")
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Greek Extended")

    # https://github.com/LettError/glyphNameFormatter/issues/38
    from glyphNameFormatter import GlyphName
    g = GlyphName(0x1FBE)
    assert g.getName() == "iotaadscript"