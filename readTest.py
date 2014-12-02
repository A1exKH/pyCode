#!/usr/bin/python

import random
import time
import os

fileName="vocabulary.txt"
delimiter=','
amountOfWods=12
delay=3

if (os.path.isfile(fileName) and os.stat(fileName).st_size !=0):
    vocabulary=open(fileName,"r")
    words=vocabulary.read().split(delimiter)
    vocabulary.close()
    random.shuffle(words)
    
    if amountOfWods>len(words):
        amountOfWods=len(words)

    for index in range(amountOfWods):
        print words[index].strip()
        if index!=len(words)-1:
            time.sleep(delay)
else:
    print "Vocabulary file is empty or doesn't exist!"
 


