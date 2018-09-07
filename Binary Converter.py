#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:31:13 2018

@author: joe-POWERmac
"""

x = float(input("Give me an number: "))
if x % 1 == 0:
    num = int(x)
    isFloat = False
else:
    p = 0
    isFloat = True
    while ((2**p)*x)%1 != 0:
        p += 1
    num = int(x*(2**p))
if num < 0:
    isNeg = True
    num = abs(num)
else: 
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isFloat:
    for i in range(p - len(result)):
        result = '0' + result
    result = result[0:-p] + '.' + result[-p:]
if isNeg:
    result = "-" + result
print(result)