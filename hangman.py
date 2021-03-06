import ast
from pprint import pprint
import random
import os

os.system('color 7')

def color(word, color='') :
	color = color.lower()
	if color == 'blue' :
		return f'\033[94m{word}\033[0m'
	elif color == 'yellow' :
		return f'\033[93m{word}\033[0m'
	elif color == 'green' :
		return f'\033[92m{word}\033[0m'
	elif color == 'red' :
		return f'\033[91m{word}\033[0m'
	else :
		return word
def display_word(word, already_guess) :
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
			print(color(f'{i}','blue'),end='')
			wrong -= 1
		print()

def print_end(correct,meaning) :
	if correct==0 :
		print(color('YOU WIN!!','green'))
	else :
		print(color('YOU LOSE!!','red'))
	print(f'word: {random_word}')
	print('meaning:')
	for description in meaning :
		print(f'\t{description}')
	print('_________________________________')

def show_not_use(word_list) :
	new_word_list = []
	for i in range(ord('a'),ord('z')+1) :
		if not chr(i) in word_list :
			new_word_list.append(chr(i))
	return new_word_list

fr = open('dict.txt','r')
line = fr.read()
fr.close()
word_list = ast.literal_eval(line)
is_play = True

while is_play :
	random_word = random.choice(list(word_list.keys()))
	wrong = 0
	correct = len(random_word)
	already_guess = []
	os.system('cls')
	print('Start!!')
	while wrong < 9 and correct > 0:
		display_man(wrong)
		display_word(random_word,already_guess)
		guess = str(input('guess character/[show]/[show_sort]/[show_invert]: ')).lower()
		os.system('cls')

		if guess == 'hint' :
			print(random_word)
			continue
		if guess == 'show_sort' :
			print(color('show: ' + str(sort(already_guess))[1:-1],'blue'))
			continue
		if guess == 'show_invert' :
			print(color('show: ' + str(show_not_use(already_guess))[1:-1],'blue'))
			continue
		if guess == 'show' :
			print(color('show: ' + str(already_guess)[1:-1],'blue'))
			continue
		if len(guess) != 1 :
			print(color('Try again, length != 1.','yellow'))
			continue
		if not ord('a') <= ord(guess) <= ord('z') :
			print(color('Try again, character including symbol.','yellow'))
			continue
		if guess in already_guess :
			print(color('Try again, you already guess.','yellow'))
			continue
		if guess in random_word :
			print(color(f'Have letter {guess}.','green'))
			correct -= random_word.count(guess)
		else :
			print(color(f'Don\'t have letter {guess}.','red'))
			wrong += 1
		already_guess.append(guess)

	print_end(correct, word_list[random_word])
	
	play_again = ''
	while play_again != 'y' and play_again != 'n' :
		play_again = input('Do you want to play again?[y/n] ').lower()
	if play_again == 'n' :
		is_play = False
print('Bye')