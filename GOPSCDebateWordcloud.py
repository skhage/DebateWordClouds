
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


candidates = set(candidates)
speakers = candidates
speakers = list(speakers)

bush = []
carson = []
cruz = []
kasich = []
rubio = []
trump = []
for line in talkingpoints:
    if line[0]=='BUSH':
        bush.append(line[1:])
    elif line[0]=='CARSON':
        carson.append(line[1:])
    elif line[0]=='CRUZ':
        cruz.append(line[1:])
    elif line[0]=='KASICH':
        kasich.append(line[1:])
    elif line[0]=='RUBIO':
        rubio.append(line[1:])
    elif line[0]=='TRUMP':
        trump.append(line[1:])
