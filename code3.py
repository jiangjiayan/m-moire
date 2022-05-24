#!/usr/bin/env python3
import math
import sys
def pollard(n):
    m = 2
    ans=[]
    max = n
    for i in range(max):
        if(i>0):
            m = pow(m,i,n)
            #print(i)
            if (math.gcd(n,m-1) != 1):
                return math.gcd(n,m-1)
print(pollard(8886599965778657))
