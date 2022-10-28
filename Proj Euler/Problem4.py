# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 16:26:36 2017

@author: admin
"""



def isPalindrome(s):
    newS= str(s)
    print (newS)
    print (newS[::-1])
    return newS == newS[::-1]



def paprod(x):
    list = []
    for x1 in range(x-100,x):
        for x2 in range(x-109,x):
            y = x1 * x2
            if isPalindrome(y):
                list.append(y)
    print (list)
    print ("Please see the larget number here: ", max(list))

if __name__=="__main__":
    paprod(1000)
    
    
'''
The palindrome can be written as: abccba Which then simpifies to: 100000a + 10000b + 1000c + 100c + 10b + a And then: 100001a + 10010b + 1100c Factoring out 11, you get: 11(9091a + 910b + 100c) So the palindrome must be divisible by 11. Seeing as 11 is prime, at least one of the numbers must be divisible by 11. So brute force in Python, only with less numbers to be checked:
Python
	
Hide Code

def c():
	max = maxI = maxJ = 0
	i = 999
	j = 990
	while (i > 100):
		j = 990
		while (j > 100):
			product = i * j
			if (product > max):
				productString = str(product)
				if (productString == productString[::-1]):
					max = product
					maxI = i
					maxJ = j
			j -= 11
		i -= 1
	return max, maxI, maxJ

Returns an answer in 0.016 secs.