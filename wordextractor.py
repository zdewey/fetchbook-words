#!/usr/bin/python

#imports all individual words from posts
#TO DO: make this work with the actual posts scraped
def import_words(filename, wordslist):
	io = open(filename)
	text = io.read()
	lines = text.split('\n')
	for w in lines:
		s = w.split(' ')
		for n in s:
			wordslist.append(n)
		wordslist.append('') #empty string indicates the end of an individual post

#deletes common words from the input list
#TO DO: implement a list of common english words and use that
def filter_common(input):
	index = 0;
	for s in input:
		if s == 'hello':
			del input[index]
		index = index+1

#produces a list of words in all scraped posts, from most to least common
#rank_list should be a list of tuples, with both the word and the number of occurrences
#can also be used to rank output from find_phrases
def rank_words(input, rank_list):
	print("TBD")

#produces a list of phrases with three or more words in them that occur more than once in dataset
#must contain at least one word that isn't on the common words list
def find_phrases(input, phrase_list):
	print("TBD")

words = list()
import_words('input.txt', words)
print(words)
filter_common(words)
print(words)