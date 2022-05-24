#!/usr/bin/env python3
import math
import random
import time 
import math
def multi(x, c, n):
    res = 0
    while c :
        if c & 1:
            res = (res + x) % n
        c >>= 1
        x = (x + x) % n
    return res
def exp(r,e,n):
    res=1
    while e:
        if e & 1:
            res =(res*r)%n
        e>>=1
        r=(r*r)%n
    return res
n=int(input("clé public de rsa:"))
e=65537
r=7
x=exp(r,e,n)
print(x)
c=int(input("une partie de chiffre:"))
y=multi(x,c,n)
print("y:",y)
u=int(input("送去混乱加密"))
m=u/r
print("m:",m)
      
