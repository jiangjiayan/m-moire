#!/usr/bin/env python3
import math
# Return the continued fractions expansions of x / y
def continuedFraction(x, y):
    ret = []
    while y:
        ret.append(x // y)
        x, y = y, x % y
    return ret
print(continuedFraction(6792605526025, 9449868410449))
def expand(ctnf):
    _ctnf = ctnf
    _ctnf.reverse()
    numerator = 0
    denominator = 1
    for x in _ctnf:
        numerator, denominator = denominator, x * denominator + numerator
    return (numerator, denominator)
        


# Return the list of n progressive fraction
def progressiveFraction(x, y):
    cfe = continuedFraction(x, y)
    cfeL = len(cfe)
    ret = []
    for i in range(1, cfeL):
        ret.append(expand(cfe[0 : i]))
    return ret
print(progressiveFraction(6792605526025, 9449868410449))
# Solve the equation: ax^2 +bx + c = 0
def solve(a, b, c):
    par = math.sqrt(b * b - 4 * a * c)
    return (-b + par) / (2 * a), (-b - par) / (2 * a)


def wienerAttack(e, n):
     res = progressiveFraction(e, n)
     for (d, k) in res:
         if k == 0 : continue
         if (e * d - 1) % k != 0:continue
         phi = (e * d - 1) / k
         p, q = solve(1, -(n - phi + 1), n)
         if p * q == n:
             print ("find it")
             print(p,q,d,k,n)
             return



wienerAttack(6792605526025, 9449868410449)

