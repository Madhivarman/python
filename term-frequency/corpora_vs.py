import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)

#documents representing strings

from  gensim import  corpora

documents = [
"Human machine interface for lab abc computer applications",
"A survey of user opinion of computer system response time",
 "The EPS user interface management system",
"System and human system engineering testing of EPS",
"Relation of user perceived response time to error measurement",
"The generation of random binary unordered trees",
"The intersection graph of paths in trees",
"Graph minors IV Widths of trees and well quasi ordering",
"Graph minors A survey"
]

#remove common words
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

#remove words that appears only once
from collections import defaultdict

frequency = defaultdict(int)
for text in texts:
   for token in text:
       frequency[token] += 1


texts = [[token for token in text if frequency[token] > 1] for text in texts]

#pretty printer
from pprint import pprint

pprint(texts)

#store in the dictionary
dictionary = corpora.Dictionary(texts)
dictionary.save('sample.dict') # for further use

print("Token and its id:")
print(dictionary.token2id)

# converts tokenized documents into vectors
corpus = [dictionary.doc2bow(text_words) for text_words in texts]
corpora.MmCorpus.serialize('sample.mm',corpus)


# for larger files to create corpus which is in localdisk
#follow this method to memory friendly,now corpus can be as large as possible

class Mycorpus(object):
    def __iter__(self):
        for line in open('sample.txt'):
            yield dictionary.doc2bow(line.lower().split())


corpus_memory_friendly = Mycorpus()

for vector in corpus_memory_friendly:
    print(vector)


corpus = corpora.MmCorpus('sample.mm')
print(corpus)
