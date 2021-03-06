#download dict here: http://www.bragitoff.com/2016/03/english-dictionary-in-csv-format/
from pprint import pprint

def is_included_symbols(word) :
	for ch in word :
		if not ord('a') <= ord(ch) <= ord('z') :
			return True
	return False

word_list = {}
for ch in range(ord('A'),ord('Z') + 1) :
	fr = open('Dictionary/' + chr(ch) + '.csv', 'r')
	lines = fr.readlines()
	for line in lines :
		line = line.replace('\n','')
		if len(line) > 0 :
			if line[0] in ['\'','\"']  :
				line = line[1:]
			if line[-1] in ['\'','\"'] :
				line = line[:-1]
		if len(line) > 0 :
			cut_index = line.find(' ')
			word = line[:cut_index].lower()
			if len(word) <= 1 or is_included_symbols(word) :
				continue
			description = line[cut_index+1:]
			if word in word_list :
				word_list[word].append(description)
			else :
				word_list[word] = [description]
	fr.close()
	#print('finished: '+chr(ch))

fw = open('dict.txt','w')
fw.write(str(word_list))
fw.close()