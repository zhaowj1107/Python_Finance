# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:03:24 2017

@author: dzhao
"""

import glob

'''
glob模块是最简单的模块之一，内容非常少。
用它可以查找符合特定规则的文件路径名。跟使用windows下的文件搜索差不多。
查找文件只用到三个匹配符：”*”, “?”, “[]”。”*”
匹配0个或多个字符；”?”匹配单个字符；”[]”匹配指定范围内的字符，如：[0-9]匹配数字。
'''

    
'''
The path has been set as the default path, so it will only read the picture in defalut path
'''


from PIL import Image


def change_resolution(patterns):
    iphone_width, iphone_height = 760, 1334
    pictures = []
    for pattern in patterns:
        pictures.extend(glob.glob(r"C:\Users\dzhao\Pictures\Camera Roll\\" + pattern))
    print(pictures)
    
    for picture in pictures:
        img = Image.open(picture)
        min_width = img.size[0] if iphone_width > img.size[0] else iphone_width
        min_height = img.size[1] if iphone_height > img.size[1] else iphone_height 
        dist = img.resize((min_width, min_height), Image.ANTIALIAS) 
        print (picture)
        dist.save(picture)
        
        
if __name__ == '__main__': 
    change_resolution(("*.jpg", "*.png"))