""" program description """
# tokenize the word
# remove the noisy words
# remove regex expression
# remove unwanted words
# abbrevate the words

# importing library we need
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer

#to see what are all the stopwords
#print(set(stopwords.words('english')))

# calling the main function
def main(input_text):
    #remove stopwords
    stop_words = set(stopwords.words('english'))
    #tokenizing the words
    word_token= word_tokenize(input_text)
    #filtering the sentence
    filtered_sentence = [w for w in word_token if not w in stop_words]
    #list
    filtered_sentence = []

    for w in word_token:
        if w not in stop_words:
            filtered_sentence.append(w)

    #join the list words
    filtered_sentence = " ".join(filtered_sentence)
    print("Filtered Sentence is :");print(filtered_sentence)


    # stemming
    ps = PorterStemmer()
    stemming_words = word_tokenize(filtered_sentence)

    #list formation
    stemming_collection_words = []

    for w in stemming_words:
        stemming_collection_words.append(ps.stem(w))

    #joining the words
    stemmed_words = " ".join(stemming_collection_words)
    print("The Sentence After Stemmed:");print(stemmed_words)


    #object standardize lookup
    __object_standardize(stemmed_words)

#__object_Standardize function called

def __object_standardize(user_input_object_expand):
    #lookup dictionary
    lookup_dict = {
        'abt': 'about', 'rt': 'Retweet', 'fb': 'Facebook', 'wanna': 'Want to',
        'dm': 'Direct message', 'ttul': 'Talk to you Later', 'tysm': 'Thankyou So much',
        'awsm': 'awesome', 'luv': 'love', 'k': 'Okay', 'msg': 'message'
    }
    user_text = user_input_object_expand.split()

    after_obj_standardize = []

    for i in user_text:
        if i.lower() in lookup_dict:
            i = lookup_dict[i.lower()]

        after_obj_standardize.append(i)

    obj_standard_word = " ".join(after_obj_standardize)
    print("After Object Standardization:");print(obj_standard_word)

def __pos_tag(text_to_post_tag):
    print("Entered:",text_to_post_tag)
    tokens = word_tokenize(text_to_post_tag)
    print("After PostTagging:");print(pos_tag(tokens))

#start of the function
user_variable = raw_input("Input the text :")

if __name__ == '__main__':
    main(user_variable)

    __pos_tag(user_variable)