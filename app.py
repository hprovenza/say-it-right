__author__ = "Hannah Provenza, Sooyoung Jeong"
import sys
import difflib
from difflib import SequenceMatcher

#audio = sys.argv[1]

#TODO: run kaldi script to get the phonetic transcription
# currently cheating with manual transcription
with open('/Users/Sooyoung/Desktop/say-it-right/transcriptions/dev/french1.txt', 'r') as f:
    transcript = f.readlines()

#TODO: align the transcription and master transcription
with open('/Users/Sooyoung/Desktop/say-it-right/transcriptions/MASTER.txt', 'r') as f:
    correct = f.readlines()
d = difflib.Differ()
diff = d.compare(correct, transcript)

devoice = {'b': 'p',
           'd':'t',
           'g': 'k',
           'v': 'f',
           'D':'T',
           'z':'s',
           'Z':'S' }

#This hasn't been finished yet
replace = {'@': 'a',
           'I': 'i',
           '3`': '3',
           'oU':'o'}


#TODO: identify the differences
i = 0
for i in range(len(correct)):
    #where i loops through the sentences
    #compares the same sentence
    s = SequenceMatcher(None, transcript[i], correct[i])
    #since opcodes returns a list you need to loop through inside
    for o in s.get_grouped_opcodes():
        #i1, i2 are indexes of transcript; j1, j2 are indexes of correct
        for tag, i1, i2, j1, j2 in o:
            #print(tag, i1, i2, j1, j2)
            print(tag, int(i1), int(i2), transcript[i][i1:i2], int(j1), int(j2), correct[i][j1:j2])
            if tag == 'replace':
                if transcript[i][i1:i2] in devoice.keys():
                    if devoice[transcript[i][i1:i2]] ==correct[i][j1:j2]:
                        #This is where the code should be to call the feedback
                        print("you should voice your sound")
                    else:
                        print("you are doing fine")
#TODO: return the errors


#TODO: print results
for x in diff:
    #print(x)
    pass
