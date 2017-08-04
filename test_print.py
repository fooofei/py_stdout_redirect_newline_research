#coding=utf-8
from __future__ import print_function
import os
import sys

# Do not use end=None, it will put '\n' in the line end auto.
print('test\r\ntest',end=u'')
# 74 65 73 74 0D 0D 0A 74 65 73 74

# Debug in python Windows source code, it run into
# builtin_print() -> PyFile_WriteObject()->file_Pyobject_Print()->
# internal_print()->string_print()

# bltinmodule.c
# fileobject.c
# object.c
# stringobject.c -> fwrite(data, 1, (size_t)size, fp);