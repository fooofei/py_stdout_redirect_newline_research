
# Research sys.stdout.write() redirect to file with the newline

I found Python2 Python3 will redirect 0x0D 0x0D 0x0A to the file,

if you use sys.stdout.write() or the print() function.


I debug the source code of Windows Python2.7.13.


It's not the Python's effect.


### The issure of python related is 

Python3 https://bugs.python.org/issue11990

Python3 https://bugs.python.org/issue13119


### Use the code snippets

```Python
import binascii

hex_print = lambda v :' '.join([v[i*2:i*2+2] for i in range(len(v)/2)])
hexlify = lambda v : hex_print(binascii.hexlify(v))


>>> print(hexlify(os.linesep),end=u'')  # on Windows
0d 0a

```


