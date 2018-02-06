import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rake_nltk import Rake 
import csv

#read csv using pandas
dataset = pd.read_csv('dataset.csv',sep=',',delimiter=None,error_bad_lines=False)

if __name__ == '__main__':
	
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

	print(sentiment_result)
	result = []
 	for statement in sentiment_result:
 		ss = st.polarity_scores(statement)
 		for k in ss:
 			result.append([k,ss[k]])

 	#print(result)


