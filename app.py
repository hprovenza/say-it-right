__author__ = "Hannah Provenza"
import sys
import difflib

audio = sys.argv[1]

#TODO: run kaldi script to get the phonetic transcription
# currently cheating with manual transcription
with open('/Users/hannahprovenza/Development/say-it-right/transcriptions/dev/french1.txt', 'r') as f:
    transcript = f.readlines()

#TODO: align the transcription and master transcription
with open('/Users/hannahprovenza/Development/say-it-right/transcriptions/MASTER.txt', 'r') as f:
    correct = f.readlines()
d = difflib.Differ()
diff = d.compare(correct, transcript)

#TODO: identify the differences


#TODO: return the errors


#TODO: print results
for x in diff:
    print(x)