#!/usr/bin/env python3
#! /usr/bin/python
from libnum import invmod
p = 3487583947589437589237958723892346254777 
q = 8767867843568934765983476584376578389
e = 65537
fn = (p-1)*(q-1)
d = invmod(e,fn)
print (d)
