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
print("Enter directory path")
dir = input()
for root, dirs, files in os.walk(dir,'r+'):
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

            #tokenizing

            #every word in outputtext- splitting wherever theres space
            #creating tokens with 16 random alphanumeric digits + 1 non alphanumeric digit
            for word in outputtext.split():
                #finding total no of words
                count = count+1
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
task1 = open("task1.txt", 'w+')

#storing frequency of each word as value in wordcount_dictionary
for d in dictionary:
    wordcount_dictionary[d] = dictionary[d][1]

#printing total word count
print ("total no of words = \t\t\t",count)
print(wordcount_dictionary)