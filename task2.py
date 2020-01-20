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

dictionary = dict()
wordcount_dictionary = dict()
stop_words = []

#storing stop words in a list
f = open("common_words.txt", "r")
if f.mode == 'r':
    for line in f:
        for word in line.split():
            stop_words += [word]
f.close()

#reading all files in dataset folder
for root, dirs, files in os.walk(r'dataset'):
    for file in files:
        with open(os.path.join(root, file), "r+") as file_p:
            outputtext = ""
            for line in file_p:
                #substituting tags with empty space
                outputtext = outputtext + re.sub("<.*?>", "", line)
                #replacing newlines,carriagereturn,commas,space,fullstops with nothing
                outputtext = outputtext.replace('\n', ' ').replace('\r',' ').replace('  ', ' ').replace('.',' ').replace(',', ' ').replace('+',' ').replace('-',' ').replace('%',' ').replace('*',' ').replace('_',' ').replace('-',' ').replace('.',' ').replace('/',' ').replace('\\',' ').replace("'",' ').replace('(',' ').replace(')',' ').replace('=',' ')
            #remove leading and trailing spaces from the string
            outputtext = outputtext.strip()
            for s in stop_words:
                outputtext = re.sub(r"\b%s\b" % s, '', outputtext)
            #tokenizing

            #every word in outputtext- splitting wherever theres space
            #creating tokens with random alphanumeric digits + non alphanumeric digit
            for word in outputtext.split():
                #finding total no of words
                count=count+1
                alphanumeric = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(16))
                non_alphanumeric = ''.join(random.choice('!<>@~`+:;()?|&*\/{}[]') for i in range(1))
                #tokenizing
                token = alphanumeric + non_alphanumeric

                #adding words,tokens and its occurence values into the dicionary
                if word in dictionary:
                    item = dictionary[word]
                    item[1] += 1
                    dictionary[word] = item
                    wordcount_dictionary[word] = item
                else:
                    list = [token, 1]
                    dictionary[word] = list
                    wordcount_dictionary[word] = 1
task2 = open("task2.txt", 'w+')

#storing frequency of each word as value in wordcount_dictionary
for d in dictionary:
    wordcount_dictionary[d] = dictionary[d][1]

#printing total word count
print ('total no of words= \t\t\t',count)

#writing total word count to task1 file
task2.write("total no of words = \t\t\t" + str(count) + "\n")

#finding dictionary length for vocabulary count
vocabulary=(len(dictionary.keys()))
print ("vocabulary= \t\t\t",vocabulary)
task2.write("vocabulary = \t\t\t" + str(vocabulary) +"\n")

#storing the top 50 frequent words in a list
print('Top 50 items are')
d=Counter(wordcount_dictionary)
newlist = d.most_common(50)

#printing the items of the list one by one
for item in newlist:
    print(a,item)
    task2.write(str(a) + "\t\t" + str(item) + "\n")
    a = a + 1

task2.close()



