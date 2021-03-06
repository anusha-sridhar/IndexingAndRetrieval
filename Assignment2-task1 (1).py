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
task1_index = dict()
dictionary = dict()
wordcount_dictionary = dict()
list = []
Filelist=[]

stop_words=[]
#storing stop words in a list
f = open("common_words.txt", "r")
if f.mode == 'r':
    for line in f:
        for word in line.split():
            stop_words += [word]

for root, dirs, files in os.walk(r'sampleset1'):
    for file in files:
        with open(os.path.join(root, file), "r+") as file_p:

            Filelist.append(file)
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
                    dictionary[word] = [str(file + ":" + "1")]


# for temp in dictionary:
#     print(temp,dictionary[temp])


print("Enter query")
querylist = input()
querylist = querylist.split(' ')
word1_weights = {}
word2_weights = {}
word3_weights = {}
totaldoc_weight = {}
doc_weight = []
i = 0

if querylist[0] in dictionary.keys():
    doclist = dictionary[querylist[0]]
    for item in doclist:
        templist = item.split(':')
        word1_weights[templist[0]] = templist[1]
else:
    word1_weights[querylist[0]] = 0


if querylist[1] in dictionary.keys():
    doclist = dictionary[querylist[1]]
    for item in doclist:
        templist = item.split(':')
        word2_weights[templist[0]] = templist[1]
else:
    word2_weights[querylist[1]] = 0


if querylist[2] in dictionary.keys():
    doclist = dictionary[querylist[2]]
    for item in doclist:
        templist = item.split(':')
        word3_weights[templist[0]] = templist[1]
else:
    word3_weights[querylist[2]] = 0


# displaying all the content in the 3 dictionary
# for temp in word1_weights:
#     print(temp,word1_weights[temp])
# print("\n")
#
# for temp in word2_weights:
#     print(temp,word2_weights[temp])
# print("\n")
#
# for temp in word3_weights:
#     print(temp,word3_weights[temp])
# print("\n")




# define Function
def my_function(dict,key):
    if key in dict.keys():
        return int(dict[key])
    else:
        return 0

for file in Filelist:
    totaldoc_weight[file] = my_function(word1_weights, file) + my_function(word2_weights,file) + my_function(word3_weights,file)

#print("displaying dictionary")
# for temp in totaldoc_weight:
#     print(temp,totaldoc_weight[temp])

# sorting dictionary
# sorting is a variable consisting of 2D array
sorting = sorted(totaldoc_weight.items(), key=lambda value: value[1],reverse=True)

print("\n\n\n sorting ")

for item in sorting:
    print(item[0],item[1])


# NOTE:::   i think it works for all inputs, better manually check it for all inputs
# NOTE:::   your task might want you to remove stop words before doing task2 , not sure , check it



# clean-up code
# remove unwanted print statements
# use  naming convention to name variables,functions,etc
# add comments where necessary, remove unwanted comments
