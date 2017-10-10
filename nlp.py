"""
    This program shows the basic implementation of tokenisation,noisy elimination
    and abbrevation of the words
"""
import nltk
import re  # importing regex library for removing regex patterns
from nltk.stem.porter import PorterStemmer #for stemming
# words to be considered in noisy list
noise_list = ["is", "a", "this", "..."]

# regex pattern to remove all expressions
regex_pattern = "#[\w]*"


# noisy removal
def __remove_noise(input_message):
    words = input_message.split()

    # noise free words
    noise_free_words = [word for word in words if word not in noise_list]
    # noise free text
    noise_free_text = " ".join(noise_free_words)

    print("Words after Noisy Elimination:");
    print(noise_free_text)

    # removing  regex pattern
    __remove_regex(noise_free_text)

# removing regex
def __remove_regex(regex_input_text):
    # finding the regex pattern
    urls = re.finditer(regex_pattern, regex_input_text)

    # iterate through the string
    for i in urls:
        regex_input_text = re.sub(i.group().strip(), '', regex_input_text)

    print("Words After removing Regex expressions:");
    print(regex_input_text)

    # calling the function for normalization
    __remove_normalization(regex_input_text)


# normalization
def __remove_normalization(normalize_input_text):

    stem = PorterStemmer()

    word = normalize_input_text

    # we can use either lemmatization or stemming

    # for stemming
    print("Word After Stemming:");
    print(stem.stem(word))

def __object_standardize(abbr_input):
    # lookup dict
    lookup_dict = {
        'abt':'about','rt':'Retweet','fb':'Facebook','wanna':'Want to',
        'dm':'Direct message','ttul':'Talk to you Later','tysm':'Thankyou So much',
        'awsm':'awesome','luv':'love','k':'Okay','msg':'message'
    }

    user_text = abbr_input.split()
    # empty list
    new_words = []

    for word in user_text:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]

        new_words.append(word)
        new_text = " " . join(new_words)

    print("Abbrevated Message is:");print(new_text)

if __name__ == '__main__':
    __remove_noise("this is #hastag from #official website Madhivarman ... is playing ")

    #object standardization
    __object_standardize("Hi I am abt to code..Do not msg me in fb")
