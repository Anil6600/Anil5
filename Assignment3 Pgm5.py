# -*- coding: utf-8 -*-
"""Copy of Untitled48.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NT5dSHjpj78z9mqnoToaEHJJS6JggRDj
"""

import random  
def Rand(start, end, num): 
    res = []     
    for j in range(num): 
  
        res.append(random.randint(start, end)) 
 
    return res
num = 50
start = 1
end = 10000
print(Rand(start, end, num))