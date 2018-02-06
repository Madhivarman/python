import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rake_nltk import Rake 
import csv
from nltk.classify import NaiveBayesClassifier

#global declaration
pos = [] #positive
neg = [] #negative
#read csv using pandas
dataset = pd.read_csv('dataset.csv',sep=',',delimiter=None,error_bad_lines=False)


def extract_keywords():
	#read data
	user_data = dataset.iloc[:,0]
	review_data = dataset.iloc[:,1]
	#new list to remove stopwords
	review = []
	for data in review_data:
		review.append(data)

	#extracting keywords
	keywords = []
	#creating object for the class
	rake = Rake()

	for data in review:
		extracted_keywords = rake.extract_keywords_from_text(data)
		ranked_phrase_keywords = rake.get_ranked_phrases()
		keywords.append(ranked_phrase_keywords)

	#print(keywords)
	sentiment_result = []
	st = SentimentIntensityAnalyzer()
	#joininig the keywords separated by commas
	for stmt in keywords:
		words = " ".join(str(e) for e in stmt)
		sentiment_result.append(words)

	#print(sentiment_result)
	result = []
 	for statement in sentiment_result:
 		ss = st.polarity_scores(statement)
 		for k in ss:
 			result.append([k,ss[k]])

 	return sentiment_result
	

def sentiment_analysis(result):

	def format_sentence(sent):
		return({word:True for word in nltk.word_tokenize(sent.decode('utf-8'))})

	#iterate through positive dataset
	with open("./pos.txt") as f:
	    for i in f: 
	        pos.append([format_sentence(i), 'pos'])

	#iterate through negative dataset
	with open("./neg.txt") as f:
	    for i in f: 
	        neg.append([format_sentence(i), 'neg'])


	training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
	print("Trained on {} instances".format(len(training)))

	test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg))]
	print("Tested on {} instances".format(len(test)))

	classifier = NaiveBayesClassifier.train(training)

	#print("Model Accuracy is:",nltk.classify.util.accuracy(classifier,training))
	#iterate through result
	senti = [] #list to store the result
	for reviews in result:
		#print(reviews)
		senti.append(classifier.classify(format_sentence(reviews)))

	return senti

def save_file(username,result):
	#zip username and result
	data = dict(zip(username,result))
	save_file = pd.DataFrame.from_dict(data=data,orient='index').to_csv('result.csv',header=False)

if __name__ == '__main__':
	filtered_result = extract_keywords()
	senti = sentiment_analysis(filtered_result)
	print(senti)
	username = dataset.iloc[:,0] #username
	save_file(username,senti)

