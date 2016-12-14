# -*- coding: latin-1 -*-
import csv
with open('Lexique381.csv') as infile:
	reader = csv.reader(infile)
	#skips a couple phrase but it's negligible comparitively
	mydict = {row[0]:row[1] for row in reader if (len(row[0].split()) ==1 and  row[0].isalpha())}

mapping = {
	'\xa7': 'o~',
	'1': '9~',
	'\xb0' : '@',
	'2' : '2',
	'5' : 'e~',
	'9' : '9',
	'8' : 'H',
	'@' : 'a~',
	'E' : 'E',
	'G' : 'N',
	'O': 'O',
	'N' : 'J',
	'S' : 'S',
	'R' : 'R',
	'Z' : 'Z',
	'a' : 'a',
	'b' : 'b',
	'e' : 'e',
	'd' : 'd',
	'g' : 'g',
	'f' : 'f',
	'i' :'i',
	'k' : 'k',
	'j' : 'j',
	'm' : 'm',
	'l' : 'l',
	'o' : 'o',
	'n' : 'n',
	'p' : 'p',
	's' : 's',
	'u' : 'u',
	't' : 't',
	'w' : 'w',
	'v' : 'v',
	'y': 'y',
	'x': 'x',
	'z': 'z'
}
phons = set()

with open('dict/lexicon.txt', 'w') as outfile:
	for k in mydict.keys():
		phon = mydict[k]
		s = ""
		for char in phon:
			s += mapping[char] + " "
			phons.add(mapping[char])
		s = s.strip()
		outfile.write(k + " " + s+'\n')
outfile.close()

with open('dict/phones.txt', 'w') as outfile:
	for p in phons:
		outfile.write(p+'\n')

outfile.close()

