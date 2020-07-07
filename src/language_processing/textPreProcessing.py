# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 06:44:38 2020
In this python file we will run the basic text processing that we do for NLP
-> Tokenisation ( using different libraries and algorithm )
-> Lemmatisation
-> Stemming using different stemmers
@author: arko
"""
import re
import string
import spacy as sp

text = "I had long wanted to watch this romantic drama (with a WWII2 setting) and, now that I have, all I can say is that it's a " \
       "veritable masterpiece of Russian cinema12! <br /><br />Soviet films are known for their overzealous propagandist approach but, " \
       "thankfully, this one's free of such emphasis - with the interest firmly on the central tragic romance between a promising artist " \
       "and a vivacious girl, doomed by the outbreak of war for which he gladly volunteers but from which he'll never return. " \
       "The girl (a remarkable performance from Tatyana Samojlova) is also loved by the young man's cousin and, " \
       "when she doesn't receive word from her boyfriend, gives in to the latter and marries him"


import string
string.punctuation
def removePunctions(txt):
  txt_nonpunct = "".join([c for c in txt if c not in string.punctuation])
  return txt_nonpunct
dataset['cleaned_col'] = dataset['col'].apply(lambda x: removePunctions(x))
dataset.head()

# data preprocessing steps
def getTransformed(text):
    
    # convert all the case to lower
    text = text.lower()
    # remove numbers
    text = re.sub(r'\d+', '', text)
    # remove punctuation 
    text = text.translate(string.maketrans("", ""), string.punctuation)
    print(text)
       
    
    
getTransformed(text)
