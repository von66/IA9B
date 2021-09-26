#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install smart_open


# In[4]:


pip install numpy scipy matplotlib ipython jupyter pandas sympy nose


# In[1]:


pip install --upgrade gensim


# In[1]:


import gensim
import pprint
from gensim import corpora
from gensim.utils import simple_preprocess


# In[4]:


doc_list = [
   "Hello, how are you?", "How do you do?", 
   "Hey what are you doing? yes you What are you doing?"
]


# In[5]:


doc_tokenized = [simple_preprocess(doc) for doc in doc_list]


# In[6]:


dictionary = corpora.Dictionary()


# In[7]:


BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]


# In[8]:


print(BoW_corpus)


# In[9]:


id_words = [[(dictionary[id], count) for id, count in line] for line in BoW_corpus]
print(id_words)


# ## Reading from a Text File

# In[10]:


import gensim
from gensim import corpora
from pprint import pprint
from gensim.utils import simple_preprocess
from smart_open import smart_open
import os
doc_tokenized = [
   simple_preprocess(line, deacc =True) for line in open(‘doc.txt’, encoding=’utf-8’)
]
dictionary = corpora.Dictionary()
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
print(BoW_corpus)


# In[ ]:




