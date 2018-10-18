
# coding: utf-8

# In[1]:


from textblob import TextBlob
import sklearn
import numpy as np
from sklearn.externals import joblib


# In[6]:


def split_into_lemmas(message):
    message=message.lower()
    words = TextBlob(message).words
    # for each word, take its "base form" = lemma 
    return [word.lemma for word in words]


def split_into_tokens(message):
    #message = unicode(message, 'utf8')  # convert bytes into proper unicode
    message=message.lower()
    return TextBlob(message).words


