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
querylist=[]

print("Enter query")
querylist = input()
querylist = querylist.split(' ')
for root, dirs, files in os.walk(r'Sampleset2'):
    for file in files:
        with open(os.path.join(root, file), "r+") as file_p:
            #variable denoting the file in the dataset
            f = f + 1
            outputtext = ""
            for line in file_p:
                #substituting tags with empty space
                outputtext = outputtext + re.sub("<.*?>", "", line)
                #replacing newlines,carriagereturn,commas,space,fullstops with nothing
                outputtext = outputtext.replace('\n', ' ').replace('\r',' ').replace('  ', ' ').replace(' . ',' ').replace(',', ' ').replace('+',' ').replace('-',' ').replace('%',' ').replace('*',' ').replace('_',' ').replace('-',' ').replace('.',' ').replace('/',' ').replace('\\',' ').replace("'",' ').replace('(',' ').replace(')',' ').replace('=',' ')
            #remove leading and trailing spaces from the string
            outputtext = outputtext.strip()

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


for temp in dictionary:
    print(temp,dictionary[temp])