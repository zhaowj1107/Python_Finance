# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:41:06 2017

@author: dzhao
"""



import pandas as pd

import re

def word_count(file_path):
    word_string = [line.rstrip('\n') for line in open(file_path)]
    words == []
    for word in word_string:
        
        tt = word.lower()
        
        t = re.sub(r'[^\w]',' ',tt)
        
        for word in t.split():
        
            words.append(word)
            
    p = pd.Series(words)
    
    freq = p.value_counts()
    
    freq = freq.ix[0:25]
    
    print (freq)

if __name__ == '__main__':

    word_count("C:/Users/dzhao/py/text.txt") 
       
'''

import pandas as pd

import re



def word_count(file_path):

    word_string = [line.rstrip('\n') for line in open(file_path)]

    words = []

    for word in word_string:

        tt = word.lower()

        t=re.sub(r'[^\w]', ' ', tt)

        for word in t.split():

            words.append(word)



    p = pd.Series(words)

    #get the counts per word

    freq = p.value_counts()

    #how many max words do we want to give back

    freq = freq.ix[0:25]

    print (freq)

if __name__ == '__main__':

    word_count("C:/Users/dzhao/py/text.txt")
    
'''