#coding=utf-8
from __future__ import print_function
import binascii
import os
import sys

curpath = os.path.dirname(os.path.realpath(__file__))

p = os.path.join(curpath,'__result')
if os.path.exists(p): os.remove(p)
with open(p,'wb') as fw:
    fw.write('test\r\ntest')

with open(p,'rb') as fr:
    c = fr.read()


hex_print = lambda v :' '.join([v[i*2:i*2+2] for i in range(len(v)/2)])
hexlify = lambda v : hex_print(binascii.hexlify(v))

print(hexlify(c),end=u'')

os.remove(p)

# 74 65 73 74 0d 0a 74 65 73 74
