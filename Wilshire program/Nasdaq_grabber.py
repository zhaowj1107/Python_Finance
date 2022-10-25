# -*- coding: utf-8 -*-
"""
Spyder Editor: David Zhao

This script is desinged for grabbing the delisting information from Nasdaq official website.
https://listingcenter.nasdaq.com/IssuersPendingSuspensionDelisting.aspx

it will generate a file with "," delimited csv file.
"""

from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import pandas as pd
import re


request = urllib.request.Request("https://listingcenter.nasdaq.com/IssuersPendingSuspensionDelisting.aspx")
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response, "lxml")
info = soup.tbody

info_str = str(info)
info_str = info_str.replace('\xa0','NA')
Delist = re.findall('<td>(.+?)</td>',info_str)
# print (Delist)

x = pd.DataFrame(np.array(Delist).reshape(int(len(Delist)/6),6),columns=["Issuer Name", "Symbol","Reason","Status","Effective Date","Form 25 Date"])

x.to_csv('C:/Users/dzhao/Desktop/grabber/Nasdaq_delist/test.csv')









'''

Old script to generate txt file without numpy and pandas

number = int(len(Delist)/6)
names = locals()
x0 = ["Issuer Name", "Symbol","Reason","Status","Effective Date","Form 25 Date"]
for i in range(number):
   i1 = i + 1
   names['x%s' % i1] = Delist[6*i:6*i+6]
#   print ('x%s' % i)
#   print (names['x%s' %i])
   
f1 = open('C:/Users/dzhao/Desktop/grabber/Nasdaq_delist/test.txt','w')    
for i in range(number):    
#    i2 = names['x%s' % i]
    for i in names['x%s' % i]:
        f1.write(i)
        f1.write('|')
    f1.write('\n')
f1.close()

'''