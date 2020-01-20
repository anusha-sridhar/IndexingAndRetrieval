import os
import re
import numpy as np
import random
import operator
import itertools
import  collections
from collections import OrderedDict
from collections import Counter
from operator import itemgetter
from itertools import islice
from collections import Counter
import math
import copy
a = 1
count = 0


nk = 0
task1_index = dict()
dictionary = OrderedDict()
wordcount_dictionary = dict()
topwordsdict = OrderedDict()
idf = OrderedDict()
tf_idf = OrderedDict()
list = []
Filelist=[]
stop_words=[]
query=[]
querylist=[]
docvec=[]
#storing stop words in a list
f = open("common_words.txt", "r")
if f.mode == 'r':
    for line in f:
        for word in line.split():
            stop_words += [word]


for root, dirs, files in os.walk(r'dataset'):
    for file in files:
        with open(os.path.join(root, file), "r+") as file_p:
            #variable denoting the file in the dataset

            Filelist.append(file)
            outputtext = ""
            for line in file_p:
                #substituting tags with empty space
                outputtext = outputtext + re.sub("<.*?>", "", line)
                #replacing newlines,carriagereturn,commas,space,fullstops with nothing
                outputtext = outputtext.replace('\n', ' ').replace('\r',' ').replace('  ', ' ').replace(' . ',' ').replace(',', ' ').replace('+',' ').replace('-',' ').replace('%',' ').replace('*',' ').replace('_',' ').replace('-',' ').replace('.',' ').replace('/',' ').replace('\\',' ').replace("'",' ').replace('(',' ').replace(')',' ').replace('=',' ')
            #remove leading and trailing spaces from the string
            outputtext = outputtext.strip()

            # removing stop words
            for s in stop_words:
                outputtext = re.sub(r"\b%s\b" % s, '', outputtext)


            for word in outputtext.split():

                if word in dictionary:
                    wordcount_dictionary[word] = wordcount_dictionary[word]+1

                    # good and find what list[-1] gives us
                    item = dictionary[word][-1]
                    if str(file) == str(item).split(":")[0] :
                        counter = str(item).split(":")[1]
                        counter = str(int(counter) + 1)
                        dictionary[word][-1] = str(file+":"+counter)
                    else:
                        list = dictionary[word]
                        list.append(str(file + ":" + "1"))
                        dictionary[word] = list
                else:
                    dictionary[word] = [str(file + ":" + "1")]
                    wordcount_dictionary[word] = 1


#storing top 1000 words in a 1D list
d = Counter(wordcount_dictionary)
newlist = d.most_common(1000)

#copying top 1000 words to another dictionary
for item in dictionary:
    for it in newlist:
        if item == it[0]:
            topwordsdict[item] = dictionary[item]
            break

dictionary.clear()
dictionary=copy.deepcopy(topwordsdict)

i=1

#extra part i added
#i'm modifying the current dictionary to the format of the table in slide 6
tempList=[]
flag=0
f = len(Filelist)
for word in dictionary:
    for fileItem in Filelist:
        for itemList in dictionary[word]:
            if fileItem == str(itemList).split(":")[0]:
                tempList.append(int(str(itemList).split(":")[1]))
                flag = 1;
        if flag == 0:
            tempList.append(int(0))
        flag = 0
    dictionary[word] = tempList
    tempList =[]

#creating idf dictionary
for item in dictionary:
    nk = 0
    freqlist = dictionary[item]
    for freq in freqlist:
        if freq != 0:
            nk = nk+1
    idf[item] = math.log10(f/nk)

#creating tf.idf dictionary
for item in idf:
    for fr in dictionary[item]:
        if item in tf_idf:
            list = tf_idf[item]
            aa = float(idf[item])*fr
            list.append(aa)
            tf_idf[item] = list
        else:
            aa = [float(idf[item])*fr]
            tf_idf[item] = aa

print('tf.idfdictionary',tf_idf)

#getting query input from user
print("Enter the query")
query = input()
querylist=query.split(' ')
queryvector=[]
i=0

print('querylist')
print(querylist)

#loading 0s in query vector
while(i<len(dictionary.keys())):
    queryvector.append(0)
    i=i+1
print('0 loaded query vector')
print(queryvector)

#modify the query vector according to query words
for q in querylist:
    counter = -1
    for word in dictionary:
        #print(word)
        counter=counter+1
        if str(word) == str(q):
            queryvector[counter] = queryvector[counter]+1
            break

print('Query vector altered according to query')
print(queryvector)

#modifying the query vector to tf.idf format
count=-1
for item in queryvector:
    count=count+1
    if item != 0:
        queryvector[count]=queryvector[count]*next(itertools.islice(idf.values(), 1,2))

print('query vector in tf.idf format')
print(queryvector)

#def to return document vector for each document from the dictionary
def create_vector(func_dictionary,n):
    tlist=[]
    for word in func_dictionary:
        tlist.append(func_dictionary[word][i])
    return tlist

#Creating document vector list and storing it in docvec which is a list of lists
i=0
while(i<f):
    t_list=create_vector(tf_idf,i)
    docvec.insert(i,t_list)
    i=i+1

print("Printing document vectors")

for item in docvec:
     print(item)

#def for computing cosine similarity
def cosine_similarity(v1,v2):
    #"compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        # if v1[i]==0 or v2[i]==0:
        #     return 0
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
        # if math.sqrt(sumxx*sumyy)==0:
        #     return 0
        try:
            div=sumxy/math.sqrt(sumxx*sumyy)
        except Exception as e:
            div=0
    return div

# print("Before dot product")
# print("printing doc vector")
# print(docvec[0])
# print("Printing query vector")
# print(queryvector)
# print("Printing dot product")
# print(cosine_similarity(docvec[0],queryvector))

#using inverted index to speed search

print('task3')
indexlist=[]
for word in querylist:
    templist=dictionary[word]
    count=-1
    i=0
    for t in templist:
        count=count+1
        if t!=0:
            if count not in indexlist:
                indexlist.append(count)

print(indexlist)

#finding cosine of query vector with all other document vectors and storing it in top10cosine list
top10cosine1={}

for j in indexlist:
    top10cosine1[j]=cosine_similarity(docvec[j],queryvector)

print("Printing cosine")
print(top10cosine1)

#finding top 10 documents

d = Counter(top10cosine1)
t_list = d.most_common(10)

for item in t_list:
    print(Filelist[item[0]])
