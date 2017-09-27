import ast
from pprint import pprint

fr = open('dict.txt','r')
line = fr.read()
fr.close()
word_list = ast.literal_eval(line)

pprint(word_list)