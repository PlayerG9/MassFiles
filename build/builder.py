r"""
pyinstaller --noconfirm --clean --windowed --hidden-import relatorio.templates.pdf --version-file "./temp/version-file.py" --add-data "./memory;memory" --name "LegalSphere" main.py

"""
import os
import sys
from pprint import pprint
from os.path import abspath, join

print("CWD:", os.getcwd())
import subprocess
import datetime
import json


BUILD = r'.\build'
CODE = r'.\NoteBook'

CMD = [
    abspath(r'.\_venv\Scripts\pyinstaller.exe'),
    '--noconfirm',
    '--clean',
    '--distpath', abspath(join(BUILD, 'dist')),
    '--workpath', abspath(join(BUILD, 'build')),
    '--specpath', abspath(join(BUILD, 'build')),

    '--runtime-hook', abspath(join(BUILD, 'sources', r'.\hooker.py')),
    # '--version-file', os.path.abspath('./temp/build/version-file.py'),
    '--icon', abspath(join(BUILD, 'sources', r'.\logo.ico')),
    '--windowed',
    # '--hidden-import', '',
    # '--add-data', f'{os.path.abspath("./memory")};memory',

    '--name', 'NoteBook',
    abspath(join(CODE, r'.\main.py'))
]
pprint(CMD)

p = subprocess.run(CMD)
if p.returncode != 0:
    sys.exit(p.returncode)

nwk = os.path.abspath(os.path.join(BUILD, 'dist', 'NoteBook'))
os.chdir(nwk)
print("CWD:", os.getcwd())
LIBDIR = 'lib'
DLLDIR = 'windll'
os.mkdir(LIBDIR)
os.mkdir(DLLDIR)

for filename in os.listdir('./'):
    if os.path.isdir(filename): continue
    filext = os.path.splitext(filename)[1]
    if filext == '.pyd':
        os.replace(filename, os.path.join(LIBDIR, filename))
    if filext == '.dll':
        if filename.startswith('py'): continue
        os.replace(filename, os.path.join(DLLDIR, filename))

# for d in ['PIL', 'tcl', 'tcl8', 'tk']:
#     os.replace(d, os.path.join(LIBDIR, d))
