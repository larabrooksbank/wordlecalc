import sys
import random
from difflib import SequenceMatcher

global turns
turns = 0

def beginning():
	print("WELCOME TO THE WORDLE CALCULATOR")
	print("***********************")
	print("ENTER GREEN, YELLOW, AND GREY LETTERS BELOW")
	print("***********************")
	print("DO NOT SEPARATE MULTIPLE LETTERS WITH SPACES OR COMMAS")


def main():
	turnsLeft = 6 - turns

	print("***********************")
	print("***********************")
	print("***********************")
	print("***********************")
	print("***********************")
	green1 = input("Enter any green letters at position 1: ")
	green2 = input("Enter any green letters at position 2: ")
	green3 = input("Enter any green letters at position 3: ")
	green4 = input("Enter any green letters at position 4: ")
	green5 = input("Enter any green letters at position 5: ")
	print("***********************")


	global greens
	greens = [green1, green2, green3, green4, green5]

	yellow1 = input("Enter any yellow letters at position 1: ")
	yellow2 = input("Enter any yellow letters at position 2: ")
	yellow3 = input("Enter any yellow letters at position 3: ")
	yellow4 = input("Enter any yellow letters at position 4: ")
	yellow5 = input("Enter any yellow letters at position 5: ")
	print("***********************")


	global yellow1List
	global yellow2List
	global yellow3List
	global yellow4List
	global yellow5List

	yellow1List = split(yellow1)
	yellow2List = split(yellow2)
	yellow3List = split(yellow3)
	yellow4List = split(yellow4)
	yellow5List = split(yellow5)

	global greyList

	grey = input("Enter all grey letters: ")

	greyList = split(grey)

	for word in greyList:
		if word in yellow5List or word in yellow4List or word in yellow3List or word in yellow2List or word in yellow1List or word in greens:
			return "ERROR! Double check!"

	for char in greyList:
		if char.isalpha() == False and char != "":
			return "ERROR! Double check!"

	for char in yellow1List:
		if char.isalpha() == False and char != "":
			return "ERROR! Double check!"

	for char in yellow2List:
		if char.isalpha() == False and char != "":
			return "ERROR! Double check!"

	for char in yellow3List:
		if char.isalpha() == False and char != "":
			return "ERROR! Double check!"

	for char in yellow4List:
		if char.isalpha() == False and char != "":
			return "ERROR! Double check!"

	for char in yellow5List:
		if char.isalpha() == False and char != "":
			return "ERROR! Double check!"

	for char in greens:
		if char.isalpha() == False and char != "":
			return "ERROR! Double check!"



	foo = open("words.txt", "r")
	global myWords
	myWords = foo.read().split()

	goo = open("winners.txt", "r")
	global winners
	winners = goo.read().split()

	for word in myWords:
		if list(word) == greens:
			final(''.join(greens))

	possibles = []

	for word in myWords:
		status = check(word)
		if status == True:
			possibles.append(word)

	if (turnsLeft <= 3 and len(possibles) > turnsLeft) or (green4 == "e" and green5 == "r"):
		filler(possibles)

	if len(possibles) > 0:
		base = 0
		baseWord = ""
		for word in possibles:
			lik = likelihood(word)
			if lik > base:
				base = lik
				baseWord = word
		return final(", ".join(possibles), baseWord)
	else:
		return("THERE ARE NO WORDS THAT MATCH :(")



def split(word):
	return [char for char in word]

def check(word):
	if (greens[0] == word[0] or greens[0] == "") and (word[0] not in greyList):
		if (word[0] in yellow1List):
			return False
		if (greens[1] == word[1] or greens[1] == "") and (word[1] not in greyList):
			if (word[1] in yellow2List):
				return False
			if (greens[2] == word[2] or greens[2] == "") and (word[2] not in greyList):
				if (word[2] in yellow3List):
					return False
				if (greens[3] == word[3] or greens[3] == "") and (word[3] not in greyList):
					if (word[3] in yellow4List):
						return False
					if (greens[4] == word[4] or greens[4] == "") and (word[4] not in greyList):
						if (word[4] in yellow5List):
							return False
						yellow1Checked = yellow1Check(word)
						yellow2Checked = yellow2Check(word)
						yellow3Checked = yellow3Check(word)
						yellow4Checked = yellow4Check(word)
						yellow5Checked = yellow5Check(word)
						if yellow1Checked and yellow2Checked and yellow3Checked and yellow4Checked and yellow5Checked:
							return True
						else:
							return False
	return False


def yellow1Check(word):
	counter = 0
	for yellow in yellow1List:
		if (yellow in word or yellow == ""):
			counter = counter + 1
	if (counter == len(yellow1List)):
		return True
	else:
		return False

def yellow2Check(word):
	counter = 0
	for yellow in yellow2List:
		if (yellow in word or yellow == ""):
			counter = counter + 1
	if (counter == len(yellow2List)):
		return True
	else:
		return False

def yellow3Check(word):
	counter = 0
	for yellow in yellow3List:
		if (yellow in word or yellow == ""):
			counter = counter + 1
	if (counter == len(yellow3List)):
		return True
	else:
		return False

def yellow4Check(word):
	counter = 0
	for yellow in yellow4List:
		if (yellow in word or yellow == ""):
			counter = counter + 1
	if (counter == len(yellow4List)):
		return True
	else:
		return False

def yellow5Check(word):
	counter = 0
	for yellow in yellow5List:
		if (yellow in word or yellow == ""):
			counter = counter + 1
	if (counter == len(yellow5List)):
		return True
	else:
		return False

def filler(possibles):
	total = 0
	for word in possibles:
		for choice in possibles:
			total = total + SequenceMatcher(None, word, choice).ratio()
	average = total / len(possibles)
	print(average)
	
	if average < 40 and average != 1.0:
		print("*** FILLER SUGGESTED! Suggested filler: " + str(fillFinder(possibles))+" ***")

def fillFinder(possibles):
	a = 0
	b = 0 
	c = 0 
	d = 0 
	e = 0 
	f = 0 
	g = 0 
	h = 0 
	i = 0 
	j = 0 
	k = 0 
	l = 0 
	m = 0 
	n = 0
	o = 0 
	p = 0  
	q = 0 
	r = 0 
	s = 0 
	t = 0 
	u = 0 
	v = 0 
	w = 0 
	x = 0 
	y = 0 
	z = 0
	for word in possibles:
		a = a + word.count("a")
		b = b + word.count("b")
		c = c + word.count("c")
		d = d + word.count("d")
		e = e + word.count("e")
		f = f + word.count("f")
		g = g + word.count("g")
		h = h + word.count("h")
		i = i + word.count("i")
		j = j + word.count("j")
		k = k + word.count("k")
		l = l + word.count("l")
		m = m + word.count("m")
		n = n + word.count("n")
		o = o + word.count("o")
		p = p + word.count("p")
		q = q + word.count("q")
		r = r + word.count("r")
		s = s + word.count("s")
		t = t + word.count("t")
		u = u + word.count("u")
		v = v + word.count("v")
		w = w + word.count("w")
		x = x + word.count("x")
		y = y + word.count("y")
		z = z + word.count("z")

	
	letters = {"a":a, "b":b, "c":c, "d":d, "e":e, "f":f, "g":g, "h":h, "i":i, "j":j, "k":k, "l":l, "m":m, "n":n, "o":o, "p":p, "q":q, "r":r, "s":s, "t":t, "u":u, "v":v, "w":w, "x":x, "y":y, "z": z}
	lettersSans0 = {key:val for key, val in letters.items() if val != 0}
	sortedLetters  = sorted(lettersSans0.items(), key=lambda x: x[1])
	specialLetters =  list(sortedLetters)[0] +  list(sortedLetters)[1] + list(sortedLetters)[2] + list(sortedLetters)[3]



	foo = open("words.txt", "r")
	global myWords
	myWords = foo.read().split()

	scores = {}

	for word in myWords:
		score = 0
		for letter in every_second_element(specialLetters):
			if letter in word:
				score = score + 1
		scores[word] = score

	max_value = max(scores, key=scores.get)
	return max_value


def every_second_element(values):
    second_values = []

    for index in range(0, len(values), 2):
        second_values.append(values[index])

    return second_values 




def likelihood(word):
	counter = 0
	dupes = []
	for letter in word:
		if word.count(letter) > 1:
			dupes.append(letter)
			counter = counter - 20
	if word in winners:
		counter = counter + 40
	for letter in word:
		if letter == "a":
			counter = counter + 43
		if letter == "b":
			counter = counter + 11
		if letter == "c":
			counter = counter + 23
		if letter == "d":
			counter = counter + 17
		if letter == "e":
			counter = counter + 57
		if letter == "f":
			counter = counter + 9
		if letter == "g":
			counter = counter + 13
		if letter == "h":
			counter = counter + 15
		if letter == "i":
			counter = counter + 39
		if letter == "j":
			counter = counter + 1
		if letter == "k":
			counter = counter + 6
		if letter == "l":
			counter = counter + 28
		if letter == "m":
			counter = counter + 15
		if letter == "n":
			counter = counter + 34
		if letter == "o":
			counter = counter + 37
		if letter == "p":
			counter = counter + 16
		if letter == "q":
			counter = counter + 1
		if letter == "r":
			counter = counter + 39
		if letter == "s":
			counter = counter + 29
		if letter == "t":
			counter = counter + 35
		if letter == "u":
			counter = counter + 19
		if letter == "v":
			counter = counter + 5
		if letter == "w":
			counter = counter + 7
		if letter == "x":
			counter = counter + 2
		if letter == "y":
			counter = counter + 9
		if letter == "z":
			counter = counter + 1
	return counter



def final(answer, best):
	return "The word can be " + answer +"." + "\nOur suggestion is " + best +"."
	

beginning()

while turns < 6:
	turns = turns + 1	
	value = main()
	if (value == "ERROR! Double check!"):
		turns = turns - 1
		print(value)
	else:
		print(value)
	print("Turns remaining: " + str(6 - turns))

