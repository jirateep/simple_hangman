#download dict here: http://www.bragitoff.com/2016/03/english-dictionary-in-csv-format/
from pprint import pprint

def is_included_symbols(word) :
	for ch in word :
		if not ord('a') <= ord(ch) <= ord('z') :
			return True
	return False

fw = open('dict.txt','w')
word_list = {}
for ch in range(ord('A'),ord('Z') + 1) :
	fr = open('Dictionary/' + chr(ch) + '.csv', 'r')
	lines = fr.readlines()
	for line in lines :
		line = line.replace('\n','')
		line = line[1:len(line)-1]
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
			
	pprint(word_list)
	input()