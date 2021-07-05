import sys
import os
from os.path import join

BASE = os.path.dirname(sys.argv[0])
LIB = join(BASE, 'lib')
sys.path.append(LIB)
# sys.path.append(os.path.join(BASE, 'lib', 'PIL'))  # useless
os.add_dll_directory(os.path.join(BASE, 'windll'))
# os.environ['TCL_LIBRARY'] = os.path.abspath(os.path.join(BASE, 'lib', 'tcl'))  # not functional
# os.environ['TK_LIBRARY'] = os.path.abspath(os.path.join(BASE, 'lib', 'tk'))


sys.path.append(join(LIB, 'tkinterweb'))
