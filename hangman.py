import ast
from pprint import pprint
import random

def display_word(word,already_guess) :
	print('GUESS THIS WORD: ',end='')
	for ch in word :
		if ch in already_guess :
			print(ch,end='')
		else :
			print('-',end='')
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
	guess = str(input('guess character: ')).lower()
	if len(guess) != 1 :
		print('ERROR: length != 1')
		continue
	if not ord('a') <= ord(guess) <= ord('z') :
		print('ERROR: character including symbol')
		continue
	already_guess.append(guess)