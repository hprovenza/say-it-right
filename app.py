__author__ = "Hannah Provenza, Sooyoung Jeong"
import sys
import difflib
from difflib import SequenceMatcher
import mistake_reporting

#audio = sys.argv[1]

#TODO: run kaldi script to get the phonetic transcription
# currently cheating with manual transcription
with open('/Users/hannahprovenza/Development/say-it-right/transcriptions/dev/french1.txt', 'r') as f:
    transcript = f.readlines()

#TODO: align the transcription and master transcription
with open('/Users/hannahprovenza/Development/say-it-right/transcriptions/MASTER.txt', 'r') as f:
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
devoice = {v: k for k, v in devoice.items()}

th_changes = {'s': 'T',
              'f': 'T'}

dh_changes = {'z': 'D',
              'v': 'D'}

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
        for code in o:
            if code[0] == 'replace':
                print(code)
                if transcript[i][code[1]] in th_changes:
                    if (th_changes[transcript[i][code[1]:code[2]]] == correct[i][code[3]:code[4]]):
                        print("unvoiced th articulation error! at char {}".format(code[3]))
                        mistake_reporting.th_articulation()
                if transcript[i][code[1]] in dh_changes:
                    if (dh_changes[transcript[i][code[1]:code[2]]] == correct[i][code[3]:code[4]]):
                        print("voiced th articulation error! at char {}".format(code[3]))
                        mistake_reporting.dh_articulation()
                if transcript[i][code[1]] in devoice:
                    if (devoice[transcript[i][code[1]:code[2]]] == correct[i][code[3]:code[4]]):
                        print("devoicing error! at char {}".format(code[3]))
                        mistake_reporting.final_devoicing()




#TODO: return the errors


#TODO: print results
for x in diff:
    #print(x)
    pass
