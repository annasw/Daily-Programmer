# Fallout Hacking minigame

import random
import string

# i want to point out that 'pimpmobile' is in enable1.txt
# i want to make it so every time you play this game,
# 'pimpmobile' is one of the words you get

f = open('enable1.txt','r')

dictionary = dict([(x,[]) for x in [4,6,9,12,15,22]])

# read in the dictionary from file
line = f.readline().strip()
while line!='':
	if len(line) in dictionary:
		dictionary[len(line)].append(line)
	line = f.readline().strip()

# get difficulty preference from player
try:
	d = int(raw_input("Difficulty (1-5)? "))
	if d==1:
		length = 4
		numWords = 5
	elif d==2:
		length = 6
		numWords = 7
	elif d==3:
		length = 9
		numWords = 10
	elif d==4:
		length = 12
		numWords = 12
	elif d==5:
		length = 15
		numWords = 15
	else:
		raise ValueError('Unacceptable difficulty entry')
except:
	print "You failed at entering a number in the suggested range."
	print "Difficulty has been set to 10."
	length = 22
	numWords = 20

# select gamewords from the dictionary entry of correct length
gameWords = []
for w in range(numWords):
	m = len(dictionary[length])
	while True:
		x = random.randint(0,m-1)
		possible = dictionary[length][x]
		if possible not in gameWords:
			gameWords.append(possible)
			break

# pick a random goal, then print all gamewords
goal = random.choice(gameWords)
for i in gameWords:
	print string.upper(i) + '\n'

# takes a word,
# returns number of letters in guess in right place
def checkGuess(word, guess):
	w = string.lower(word)
	g = string.lower(guess)
	if len(g)>length:
		g = g[:length]
	score = 0
	
	# it's unnecessary to do this way;
	# i can cut the if len(g)>length and just run this
	# through range(len(w))
	for idx in range(len(g)):
		if g[idx]==w[idx]:
			score +=1
	return score

# play game
guesses = 4
while guesses>0:
	text = "Guess (%d left)? " % guesses
	guess = raw_input(text)
	score = checkGuess(goal,guess)
	print '' + str(score) + '/'+ str(len(goal)) + ' correct'
	if score == len(goal) == len(guess):
		print "You win!"
		break
	elif guesses==1:
		print "You lose!"
	guesses -= 1
