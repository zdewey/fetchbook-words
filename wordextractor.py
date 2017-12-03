#!/usr/bin/python

import string

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

#formats words - sets all to lowercase, removes punctuation
def format_words(input, output):
	for s in input:
		f_string = s.translate(None, string.punctuation)
		output.append(f_string.lower())

#deletes common words from the input list
#TO DO: implement a list of common english words and use that
def filter_common(input):
	index = 0;
	comlist = open('common.txt') #common.txt is a list of common words to filter out, one per line
	text = comlist.read()
	common_list = text.split('\n')
	delete = list() #stores indicies of words to be deleted
	#print(common_list)
	for s in input:
		for c in common_list:
			if s == c:
				delete.insert(0,index)
				break
		index = index+1
	for i in delete:
		del(input[i])

#produces a list of words in all scraped posts, from most to least common
#rank_list should be a list of tuples, with both the word and the number of occurrences
#can also be used to rank output from find_phrases
def rank_words(input, rank_list, output_file):
	rank_list = {}
	for s in input:
		if s == '':
			continue
		if s in rank_list:
			rank_list[s] += 1
		else:
			rank_list[s] = 1
	outfile = open(output_file,'w')
	itemlist = list()
	for key, value in sorted(rank_list.iteritems(), key=lambda (k,v): (v,k)):
		itemlist.insert(0,"%s: %s\n" % (key,value)) #reverse output to sort greatest->least
	for item in itemlist:
		outfile.write(item)

def rank_phrases(input, rank_list, output_file):
	rank_list = {}
	for s in input:
		if s in rank_list:
			rank_list[s] += 1
		else:
			rank_list[s] = 1
	for key in rank_list.keys():
		if rank_list[key] <= 3:
			del rank_list[key]
			continue
		phrasewords = key.split(' ')
		filter_common(phrasewords)
		if len(phrasewords) == 1: #only common words in phrase
			del rank_list[key]
			
	outfile = open(output_file,'w')
	itemlist = list()
	for key, value in sorted(rank_list.iteritems(), key=lambda (k,v): (v,k)):
		itemlist.insert(0,"%s: %s\n" % (key,value)) #reverse output to sort greatest->least
	for item in itemlist:
		outfile.write(item)

#produces a list of phrases with three or more words in them that occur more than once in dataset
def find_phrases(filename, ngram_list):
	io = open(filename)
	text = io.read()
	lines = text.split('\n')
	lines_format = list()
	format_words(lines,lines_format)
	for i in range(3,7): #run iteratively for desired range of phrase length
		for s in lines_format: #take each post one at a time instead of all at once
			wordsinline = s.split(' ')
			delete = list()
			index = 0
			for word in wordsinline: #remove all empty strings
				if word == '':
					delete.insert(0,index)
				index = index+1
			for d in delete:
				del(wordsinline[d])
			if(len(wordsinline) < i): #not enough words for ngram!
				continue
			for start_index in range(0,len(wordsinline)-(i-1)): #loop over each line, picking each subset of X words
				ngram = ""
				for index in range(start_index, start_index+i):
					ngram += wordsinline[index] + " "
				ngram_list.append(ngram)


words = list()
import_words('input.txt', words)
words_formatted = list()
format_words(words, words_formatted)
words = words_formatted
filter_common(words)
ranklist = {}
rank_words(words, ranklist, 'rankedwords.txt')
phrases = list()
find_phrases('input.txt', phrases)
phraselist = {}
rank_phrases(phrases, phraselist, 'rankedphrases.txt')