#import necessary libraries in the file
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn 
import os
from collections import defaultdict
import spacy

#load English language
nlp = spacy.load('en')

#import the file path
file_path = "r8-test-stemmed.txt"

#open the file
file_data = open(file_path).read()
#separate the file by new line
file_data = file_data.split("\n")

print("The total length of the list is:\t{}".format(len(file_data)))

"""
	Iterate through each document list and find each semantic score
	Find Permutation of semantic calculations first in the document
	Remove stopwards and noisy words
	Using DFS we consider each word as a node and connect each node to other node  and 
	form as a network topology
"""

class Graph:
	#constructor

	def __init__(self):
		#default dictionary to store the graph
		self.graph = defaultdict(list) #defaultdict as list

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def find_similarity_score(self,network):
		#the networks is in format type(Class <str>, class <list>)
		#find the length of the network so we can find semantic score for last one
		len_def_dict = len(network)
		keep_track = 1 #initial value

		for k,v in network.items():
			if keep_track == len_def_dict:
				#do the your semantic stuff right here and increment the pointer after that
				focus_word = nlp(u'{}'.format(k))
				for check_words in v:
					word = nlp(u'{}'.format(check_words))
					score = focus_word.similarity(word)
					#open a file and write the sentence
					with open('result.txt',"a") as fp:
						fp.write("{},{},{}".format(focus_word,check_words,score))
						fp.write("\n")
					
		
			keep_track += 1 #increment the pointer



#create object for the graph
g = Graph()

"""for word in range(len(sample)):
	focus_word = sample[word]
	focus_word_index = sample.index(focus_word)
	for ind_words in range(len(sample)):
		if  ind_words == focus_word_index:
			pass
		else:
			g.addEdge(focus_word,sample[ind_words])

	#now calculate the semantic score
	g.find_similarity_score(g.graph)"""

for each_doc in file_data:
	#tokenize the word and find the length of the list
	word_tokens = word_tokenize(each_doc)
	#find the length of the list
	length_documents = len(set(word_tokens)) #remove duplicates in the list
	#iterate through each word and form the network
	i=1
	for each_word_index in range(length_documents):
		#get the word as focus_word
		focus_word = word_tokens[each_word_index]
		#run another loop to iterate through each word
		focus_word_index = word_tokens.index(focus_word) #get focus word index
		#run a loop to iterate
		for word_index in range(length_documents):
			#run a condition to find a focus word
			if(word_index == focus_word_index):
				pass #do nothing
			else:
				g.addEdge(focus_word,word_tokens[word_index]) #add edge between each word_token

		#connection is made with each words and now plot the syntax score
		#the type of graph is default dictionary
		g.find_similarity_score(g.graph)
		
		if(i%500 == 0):
			print("Finished calculating Semantic score for {} documents".format(i))

	i+=1 #increment the value i
	
	g.graph = defaultdict(list) #empty the graph list

print("The length of the Graph network is:\t{}".format(len(g.graph))) # the length of the graph network is 7242
