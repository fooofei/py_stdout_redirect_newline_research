#coding=utf-8

import os
import sys

sys.stdout.write('test\r\ntest')
# 74 65 73 74 0D 0D 0A 74 65 73 74


# Debug in python Windows source code, it not run into as print()
# builtin_print() -> PyFile_WriteObject()->file_Pyobject_Print()->
# internal_print()->string_print()