# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 18:30:42 2017

@author: admin
"""

import math 
 
def isPrime(n): 
    if n <= 1: 
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: 
            return False
        return True



list = [i for i in range(1,21)]
z = [isPrime(x) for x in list]
list=[i for i in list if z[i-1]]
PF = 1
for i in list:
    PF = PF * i
PF = PF/15
x = 1

while True:
    if PF % 4 == 0 and PF % 6 == 0 and PF % 8 == 0 and PF % 10 == 0 and PF % 12 == 0 and PF % 14 == 0 and PF % 15 == 0 and PF % 16 == 0 and PF % 18 == 0 and PF%20 ==0:
        break
    PF = PF * x
    print (PF)
    x = x + 1    


"""
if __name__=="__main__":
    SmallestMultiple(10)
    print (list)
    
"""