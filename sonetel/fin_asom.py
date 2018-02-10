#necessary libraries
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import os
import csv
import textblob
from textblob import TextBlob 

filepath = '/home/madhi/Documents/python programs/intern/sonetel/datasets'
total_datasets = os.listdir(filepath)

#append all datas to the list
data_list = []
#read all dataset and create new file dataframe
for datas in total_datasets:
    file = open(filepath+"/"+datas,"r")
    reader = csv.reader(file,delimiter=',')
    for values in reader:
        data_list.append(values)
    file.close()

#convert the data_list into a dataframe
dataframe = pd.DataFrame(data=data_list,columns=["name","review"])

#print(dataframe.head())

#removing punctuations and unnecessary tokens,regex expression,doublequotes from the review statements
review = dataframe.review
remove_list = ["</br>","\n"]
#review_cleaned
review_cleaned = []
for clean_review in review:
    #word tokenize
    words = nltk.word_tokenize(clean_review)
    words = [word.lower() for word in words if word.isalpha()]
    words = " ".join(words)
    review_cleaned.append(words)

dataframe['review'] = review_cleaned #now data is cleaned
#print(dataframe.head())
save_file = pd.DataFrame(data=dataframe).to_csv('asom.csv')

review = dataframe.review
tagged_review_list = [] #list

def posTag(review):
	for data in review:
		text = word_tokenize(data)
		tagged_review_list.append(nltk.pos_tag(text))

	return tagged_review_list

#filtering the postag
def filter_taging(taged_sentence):
	aspect_element = [] #list to store the aspect element
	adverb_element = [] #list to store the adverb element

	for text_tag_list in taged_sentence:
		for word,tag in text_tag_list:
			if tag in ['NNS','NN','NNP']:
				aspect_element.append(word)
			if tag in ['JJ','JJR']:
				adverb_element.append(word)

	return aspect_element,adverb_element



#main function starts
tagged_user_input = posTag(review)
aspect,adverb = filter_taging(tagged_user_input)


#print(resutlt_dict) 
#apply stopwords from the aspect,adverb
stopwords = set(stopwords.words('english'))
aspect_wo_sw = [] #list to store without stopwords
adverb_wo_sw = [] #list to store without stopwords

for words in aspect:
	word = nltk.word_tokenize(words)
	for w in word:
		if w not in stopwords:
			aspect_wo_sw.append(w)

for words in adverb:
	word = nltk.word_tokenize(words)
	for w in word:
		if w not in stopwords:
			adverb_wo_sw.append(w)

#print(aspect_wo_sw)

#picking top aspects from the list
from collections import Counter
freqs = Counter(aspect_wo_sw)
#print(freqs)

"""
	picking top aspects from the freq list to analyse the 
	aspect sentiment
"""
top_aspects = ["service","customer","business","support",
"quality","services","system","price","payment","issues","experience","money","feature"]

"""
	iterate through the customer review if they mentioned about aspects 
"""
check_senti = [] #list
for cmnt in review:
	#word_tokenize to find the aspect element
	tokens = nltk.word_tokenize(cmnt)
	check_senti.append(tokens)

#pop the first element from the list
check_senti.pop(0)
#iteration
customer_review = [] #storing the result
result = []
#removing empty list
#this list contain all words from the reviews
list_one =  [x for x in check_senti if x != []]
print(len(list_one))
user_id = 1

for inner_list in list_one:
	list_len = len(inner_list)
	for x in inner_list:
		if x in top_aspects:
			pointer_pos = inner_list.index(x)
			next_pos = pointer_pos + 1
			while(next_pos < list_len):
				adv = inner_list[next_pos]
				if adv in adverb:
					test = TextBlob(adv)
					senti_pol = test.sentiment.polarity
					if senti_pol < 0:
						sentiment = "negative"
					else:
						sentiment = "positive"
					result.append({str(user_id)+","+x+":"+sentiment})
				next_pos += 1
		break
	user_id += 1


print(result)