import os
import os.path
import sys
import shutil

def mkdir():
	dirs = ["data", "data/test", "data/train"]
	for d in dirs:
		os.system("mkdir " +d)

mkdir()

test = []
train = []


root = os.getcwd()
path = root+"/data"

for folder in os.listdir(path):
	if folder == "test_audio":
		for entry in os.listdir(path+'/'+folder):
			if not entry.startswith('.'):
				for f in os.listdir(path+'/'+folder+'/'+entry):
					if f == "etc":
						prompt = open(path+'/'+folder+'/'+entry+'/etc/PROMPTS', 'r')
						for line in prompt.readlines():
							if "anonymous" in line:
								pass
							else:
								test.append(line)
	if folder == "train_audio":
		for entry in os.listdir(path+'/'+folder):
			if not entry.startswith('.'):
				for f in os.listdir(path+'/'+folder+'/'+entry):
					if f == "etc":
						prompt = open(path+'/'+folder+'/'+entry+'/etc/PROMPTS', 'r')
						for line in prompt.readlines():
							if "anonymous" in line:
								pass
							else:
								train.append(line)

def make_text(filenames, data_path):
	results = []
	for f in filenames:
		parse = f.split(None, 1)
		base_name = get_uttid(f)
		trans = parse[1]
		if not base_name[0].isdigit():
			results.append("{} {}".format(base_name, trans))
	with open(data_path+"/text", 'w') as text:
		text.write('\n'.join(sorted(results)))


def wav_scp(filenames, data_path):
	results = []
	for f in filenames:
		base_name = get_uttid(f)
		p = getpath(f)
		if not base_name[0].isdigit():
			results.append("{} {}".format(base_name, path+p))
		
	with open(data_path+"/wav.scp", 'w') as text:
		text.write('\n'.join(sorted(results)))



def utt2spk(filenames, data_path):
	results = []
	for f in filenames:
		uttid = get_uttid(f)
		spkid = get_spkid(f)
		if not uttid[0].isdigit():
			results.append("{} {}".format(uttid, spkid))
	with open(data_path+"/utt2spk", 'w') as text:
		text.write('\n'.join(sorted(results)))

def spk2utt():
	data_paths = ["data/train", "data/test"]
	for path in data_paths:
		os.system('utils/utt2spk_to_spk2utt.pl '+ path+'/utt2spk > ' + path+'/spk2utt')

def fix():
	data_paths = ["data/train", "data/test"]
	for path in data_paths:
		os.system('utils/fix_data_dir.sh ' + path)

def get_uttid(wave_filename):
	fileid = get_fileid(wave_filename)
	spkid = get_spkid(wave_filename)
	return spkid+'-'+fileid


def get_fileid(wave_filename):
	base = wave_filename.split(None, 1)[0]
	f = base.split(os.sep)
	file_basename = f[-1]
	return file_basename


def get_spkid(wave_filename):
	b = wave_filename.split(None, 1)[0]
	base = b.split(os.sep)[0]
	split = base.split("-")
	spkid = split[2]+"-"+split[1]+"-"+split[0]
	return spkid

def getpath(filename):
	base = filename.split(None, 1)[0]
	split = base.split(os.sep)
	path = "/"+split[0]+"/wav/"+split[2]+".wav"
	return path


files = [test, train]
p = ["test", "train"]
i = 0
for f in files:
	make_text(f, path+'/'+p[i])
	wav_scp(f, path+'/'+p[i])
	utt2spk(f,path+'/'+p[i])
	i += 1

fix()
#Create the test and train set
# i = 0
# for folder in os.listdir(path):
# 	if not folder.startswith('.'):
# 		if i%2 == 0:
# 			if(not os.path.exists(root+"/data/test/"+folder)):
# 				shutil.copytree(path+folder, root+"/data/test/"+folder)
# 				test.append(root+"/data/test/"+folder)
# 				i+= 1
# 		else:
# 			if(not os.path.exists(root+"/data/train/"+folder)):
# 				shutil.copytree(path+folder, root+"/data/train/"+folder)
# 				train.append(root+"/data/test/"+folder)
# 				i+= 1
