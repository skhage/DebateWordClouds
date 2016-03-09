
# coding: utf-8

# In[4]:

from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[13]:

url = urlopen('https://www.washingtonpost.com/news/the-fix/wp/2016/02/13/the-cbs-republican-debate-transcript-annotated')
bsObj = BeautifulSoup(url.read(),'html.parser')
print(bsObj.text)


# In[20]:

text = bsObj.find(text=True,'p')
print(text)

