# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:29:01 2017

@author: dzhao
"""


import random, string

def random_str(num, length = 7):
    f = open("C:/Users/赵伟健/OneDrive/Python/Python 练习册/Running_result.txt", 'w')
    for i in range(num):
        chars = string.ascii_letters + string.digits
        s = [random.choice(chars) for i in range(length)]
        f.write(''.join(s) + '\n')
    f.close()
    
'''
当被引用时，不执行此模块，当单独运行调试时，执行random_str(200)

引用时，__name__=文件名，Play1
运行调试时，__name__ = '__main__'

'''

if __name__ == '__main__':

    random_str(200)