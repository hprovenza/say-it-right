__author__ = "Hannah Provenza"

import urllib

for x in range(1,64):
    filename = "french" + str(x) + ".mp3"
    print filename
    u = urllib.URLopener()
    u.retrieve("http://accent.gmu.edu/soundtracks/" + filename, filename)