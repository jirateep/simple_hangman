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

def display_man(wrong) :
	man = [[' _________',''],
		   [' |        ','|'],
		   [' |        ','O'],
		   [' |        ','|'],
		   [' |       ','/|\\'],
		   [' |        ','|'],
		   [' |       ','/\\'],
		   ['=+====','']
		  ]
	for tmp in man :
		print(tmp[0],end='')
		for i in tmp[1] :
			if wrong <= 0 :
				break
			print(i,end='')
			wrong -= 1
		print()

fr = open('dict.txt','r')
line = fr.read()
fr.close()
word_list = ast.literal_eval(line)
random_word = random.choice(list(word_list.keys()))
print(random_word)
wrong = 0
already_guess = []
while wrong < 9 :
	display_man(wrong)
	display_word(random_word,already_guess)
	guess = str(input('guess character: ')).lower()
	if len(guess) != 1 :
		print('Try again, length != 1.')
		continue
	if not ord('a') <= ord(guess) <= ord('z') :
		print('Try again, character including symbol.')
		continue
	if guess in already_guess :
		print('Try again, you already guess.')
		continue
	if guess in random_word :
		print(f'Have letter {guess}.')
	else :
		print(f'Don\'t have letter {guess}.')
		wrong += 1
	already_guess.append(guess)