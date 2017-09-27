import ast
from pprint import pprint
import random

fr = open('dict.txt','r')
line = fr.read()
fr.close()
word_list = ast.literal_eval(line)
random_word = random.choice(list(word_list.keys()))

print(random_word)
#pprint(word_list)