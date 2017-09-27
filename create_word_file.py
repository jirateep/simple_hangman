#download dict here: http://www.bragitoff.com/2016/03/english-dictionary-in-csv-format/

fw = open('dict.txt','w')
word_list = []
for char in range(ord('A'),ord('Z') + 1) :
	fr = open('Dictionary/' + chr(char) + '.csv', 'r')
	lines = fr.readlines()
	for line in lines :
		line = line.replace('\n','')
		line = line[1:len(line)-1]
		if len(line) > 0 :
			cut_index = line.find(' ')
			word = line[:cut_index]
			if len(word) <= 1 :
				continue
			description = line[cut_index+1:]
			word_list.append({'word':word, 'description':[description]})
			print(word_list)
			input()