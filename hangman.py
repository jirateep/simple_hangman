import ast
from pprint import pprint
import random

def display_word(word,already_guess) :
	print('GUESS THIS WORD: ',end='')
	for ch in word :
		if ch in already_guess :
			print(ch,end='')
		else :
			print('_',end='')
	print()

fr = open('dict.txt','r')
line = fr.read()
fr.close()
word_list = ast.literal_eval(line)
random_word = random.choice(list(word_list.keys()))
print(random_word)
wrong = 0
already_guess = []
while wrong < 10 :
	display_word(random_word,already_guess)
	guess = input('guess character: ')
	already_guess.append(guess)