from bs4 import BeautifulSoup as bs
import urllib2
import requests
import csv
import pandas as pd

#page url
page = requests.get("https://www.trustpilot.com/review/www.sonetel.com")

soup = bs(page.content,'html.parser')
page_content = soup.find_all('div',class_="review-stack")

usernames = [] #usernamelist

#finding all comments
for names in page_content:
	name_tags = names.find_all("a",class_="user-review-name-link")
	names = name_tags[0].find("span")
	usernames.append(names)

#print(usernames) #print all usernames


user = []
#to remove unwanted  literals
for words in usernames:
	dup = str(words)
	dup_list = list(dup)
	#length of the strings
	length = len(dup_list)
	start = length - 7
	#delete unwanted lists
	del(dup_list[start:length])
	del(dup_list[0:15])
	word = "".join(str(e) for e in dup_list)
	user.append(word)

#print(user)

# extracting user reviews 
review = []
for reviews in page_content:
	review_tags = reviews.find_all("div",class_="review-body")
	user_reviews = review_tags[0]
	review.append(user_reviews)

review_words = [] #list

for views in review:
	dup_rev = str(views)
	dup_rev_list = list(dup_rev)
	#length 
	length_rev = len(dup_rev_list)
	start_rev = length_rev - 6
	#delete 
	del(dup_rev_list[start_rev:length_rev])
	del(dup_rev_list[0:50]) #removing \t too
	reviews_words = "".join(str(e)  for e in dup_rev_list)
	review_words.append(reviews_words)

#print(review_words)	
#joining the usernames and their corresponding reviews

result = dict(zip(user,review_words))
#print(result)

save_file = pd.DataFrame.from_dict(data=result,orient='index').to_csv('dataset.csv',header=False)