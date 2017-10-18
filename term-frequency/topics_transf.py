import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s:%(message)s',level=logging.INFO)

#fireup gensim and use that corpus we generate in previous file

from gensim import corpora,models,similarities

import os
if(os.path.exists("sample.mm")):
    dictionary = corpora.Dictionary.load('sample.dict')
    corpus = corpora.MmCorpus('sample.mm')
else:
    print("Generate Corpora and Vector spacce first")

#describe relationship between words and use them more semantic way
tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print(doc)

#tf-idf by LDA technique
#semantic analysis by LSI technique

lsi = models.LsiModel(corpus_tfidf,id2word=dictionary,num_topics=2)
corpus_lsi = lsi[corpus_tfidf]

print("Word range near 1 means similar,range near 0 means different")
print("-------------------------------------------------------------")
lsi.print_topics(2)

for doc in corpus_lsi:
    print(doc)

#save the lsi model
lsi.save('model.lsi')
lsi = models.LsiModel.load('model.lsi')