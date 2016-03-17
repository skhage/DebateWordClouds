
# coding: utf-8

# In[4]:

from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[13]:

url = urlopen('https://www.washingtonpost.com/news/the-fix/wp/2016/02/13/the-cbs-republican-debate-transcript-annotated')
bsObj = BeautifulSoup(url.read(),'html.parser')
print(bsObj.text)


# In[20]:

soundbytes = bsObj.findAll("p",{"class":""})[4:]

talkingpoints = []
for line in soundbytes:
    line = line.text
    line = line.split(":")
    if line[0] != '(COMMERCIAL BREAK)' and line[0] != '(BELL RINGING)' and line[0] != '(APPLAUSE)':
        talkingpoints.append(line)

