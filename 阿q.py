
# coding: utf-8

# In[25]:

import jieba
import random 
import datetime

random.seed(datetime.datetime.now())
text=open("阿q .txt","r").read()



def wordsum(wv):
    sum=0 
    for word,value in wv.items():
        sum+=value
    return sum

def randomword(wv):
    randindex=random.randint(1,wordsum(wv))
    for word,value in wv.items():
        randindex-=value
        if randindex<=0:
            return word

def wordict(text):
    text=text.replace("\n","")
    text=text.replace("\"","")
    text=text.replace(" ","")
    
    
    punctuation=['，','。','《','》','：','！','？',";"]
    for symbol in punctuation:
        text=text.replace(symbol,""+symbol+"")
    
    
        
        
        
    words=jieba.cut(text, cut_all=False)
    wordlist=[]
    for item in words:
        wordlist.append(item)
    
    
    wordict={}
    for i in range(1,len(wordlist)):
        if wordlist[i-1] not in wordict:
            wordict[wordlist[i-1]]={}
        if wordlist[i] not in wordict[wordlist[i-1]]:
            wordict[wordlist[i-1]][wordlist[i]]=0
        wordict[wordlist[i-1]][wordlist[i]]+=1
    
    return wordict

wordict=wordict(text)

lenght=300
chain=""
currentWord="阿"
for i in range(0,lenght):
    chain+=currentWord+" "
    currentWord=randomword(wordict[currentWord])

print(chain)



# In[ ]:



