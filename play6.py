# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:45:19 2017

**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt.
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

@author: dzhao
"""

import re
import glob
from collections import Counter

files = glob.glob("*.txt") # files as a list

for file in files: # file as the path
    print (file)
    with open(file, "r") as f:
        txt = f.read()
        reg = re.compile(r'[\w]+')
        wordlist = reg.findall(txt)
        cntObj = Counter(wordlist)
        print(cntObj.most_common(1))