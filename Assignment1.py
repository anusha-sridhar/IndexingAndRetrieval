import os
import re
import random
import operator
import itertools
import  collections
from collections import OrderedDict
from collections import Counter
from operator import itemgetter
from itertools import islice
from collections import Counter

a = 1
count = 0
f=0
task1_index=dict()
dictionary = dict()
wordcount_dictionary = dict()
list = []
stop_words=[]
#storing stop words in a list
f = open("common_words.txt", "r")
if f.mode == 'r':
    for line in f:
        for word in line.split():
            stop_words += [word]
for root, dirs, files in os.walk(r'Sampleset2'):
    for file in files:
        with open(os.path.join(root, file), "r+") as file_p:

            outputtext = ""
            for line in file_p:
                #substituting tags with empty space
                outputtext = outputtext + re.sub("<.*?>", "", line)
                #replacing newlines,carriagereturn,commas,space,fullstops with nothing
                outputtext = outputtext.replace('\n', ' ').replace('\r',' ').replace('  ', ' ').replace(' . ',' ').replace(',', ' ').replace('+',' ').replace('-',' ').replace('%',' ').replace('*',' ').replace('_',' ').replace('-',' ').replace('.',' ').replace('/',' ').replace('\\',' ').replace("'",' ').replace('(',' ').replace(')',' ').replace('=',' ')
            #remove leading and trailing spaces from the string
            outputtext = outputtext.strip()
            for s in stop_words:
                outputtext = re.sub(r"\b%s\b" % s, '', outputtext)

            print(outputtext)
            for word in outputtext.split():

                if word in dictionary:
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
                    #list.append(str(file + ":" + "1"))
                    dictionary[word] = [str(file + ":" + "1")]
                    #list=[]
print("Enter query")
querylist = input()
print(querylist)
querylist = querylist.split(' ')
print(querylist)
word1_weights = {}
word2_weights = {}
word3_weights = {}
totaldoc_weight = {}
doc_weight = []
i = 0

#saving each word's value in a separate list
if querylist[0] in dictionary.keys():
    doclist = dictionary[querylist[0]]
    for item in doclist:
        templist = item.split(':')
        word1_weights[templist[0]] = templist[1]
        print('word1_weights:')
        print(word1_weights)
else:
    word1_weights[querylist[0]] = 0
    print(word1_weights)

if querylist[1] in dictionary.keys():
    doclist = dictionary[querylist[1]]
    for item in doclist:
        templist = item.split(':')
        word2_weights[templist[0]] = templist[1]
        print('word2_weights:')
        print(word2_weights)
else:
    word2_weights[querylist[1]] = 0
    print(word2_weights)

if querylist[2] in dictionary.keys():
    doclist = dictionary[querylist[2]]
    for item in doclist:
        templist = item.split(':')
        word3_weights[templist[0]] = templist[1]
        print('word3_weights:')
        print(word3_weights)
else:
    word3_weights[querylist[2]] = 0
    print(word3_weights)

for key in word1_weights:
    if key in word2_weights.keys() and word3_weights.keys():
        totaldoc_weight[key] = word1_weights[key] + word2_weights[key] + word3_weights[key]
        word1_weights.pop(key)
        word2_weights.pop(key)
        word3_weights.pop(key)
    else:
        if key in word2_weights.keys():
            totaldoc_weight[key] = word1_weights[key] + word2_weights[key]
            word1_weights.pop(key)
            word2_weights.pop(key)
        else:
            if key in word3_weights.keys():
                totaldoc_weight[key] = word1_weights[key] + word3_weights[key]
                word1_weights.pop(key)
                word3_weights.pop(key)
        totaldoc_weight[key] = word1_weights[key]

for key in word2_weights:
    if key in word3_weights.keys():
        totaldoc_weight[key] = word2_weights[key] + word3_weights[key]
        word2_weights.pop(key)
        word3_weights.pop(key)
    else:
        totaldoc_weight[key] = word2_weights[key]

for key in word3_weights:
    totaldoc_weight[key] = word3_weights[key]

print(totaldoc_weight[key])
print('aaa')






