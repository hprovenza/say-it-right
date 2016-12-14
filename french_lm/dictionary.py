import csv
with open('Lexique381.csv') as infile:
	reader = csv.reader(infile)
	#skips a couple phrase but it's negligible comparitively
	mydict = {row[0]:row[1] for row in reader if len(row[0].split()) ==1}

#print(mydict)
phons = set()

with open('dict/lexicon.txt', 'w') as outfile:
	for k in mydict.keys():
		phon = mydict[k]
		s = ""
		for char in phon:
			s += char + " "
			phons.add(char)
		s = s.strip()
		outfile.write(k + " " + s+'\n')
outfile.close()

with open('dict/phones.txt', 'w') as outfile:
	for p in phons:
		outfile.write(p+'\n')

outfile.close()

