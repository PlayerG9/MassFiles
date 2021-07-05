r"""
pyinstaller --noconfirm --clean --windowed --hidden-import relatorio.templates.pdf --version-file "./temp/version-file.py" --add-data "./memory;memory" --name "LegalSphere" main.py

"""
import os
import sys
from pprint import pprint
from os.path import abspath, join

print("CWD:", os.getcwd())
import subprocess


APPNAME = "NoteBook"

BUILD = abspath(r'.\build')
CODE = abspath(r'.\NoteBook')
TARGET = join(BUILD, 'dist', APPNAME)

CMD = [
    abspath(r'.\_venv\Scripts\pyinstaller.exe'),
    '--noconfirm',
    '--clean',
    '--distpath', join(BUILD, 'dist'),
    '--workpath', join(BUILD, 'build'),
    '--specpath', join(BUILD, 'build'),

    '--runtime-hook', join(BUILD, 'sources', r'.\hooker.py'),
    '--additional-hooks-dir', join(BUILD, 'sources'),
    # '--version-file', os.path.abspath('./temp/build/version-file.py'),
    '--icon', join(BUILD, 'sources', r'.\logo.ico'),
    '--windowed',
    # '--hidden-import', '',
    # '--add-data', f'{os.path.abspath("./memory")};memory',
    # '--add-data', f'{CODE};NoteBook',


    '--name', APPNAME,
    abspath('runner.py')
]
pprint(CMD)

p = subprocess.run(CMD)
if p.returncode != 0:
    sys.exit(p.returncode)


import py_compile
BASE = './NoteBook'
os.mkdir(join(TARGET, APPNAME))
for root, dirs, files in os.walk(BASE):
    if root.endswith(('__pycache__', 'plugins')): continue
    rel = os.path.relpath(root, BASE)
    for dir in dirs:
        if dir == '__pycache__': continue
        os.mkdir(abspath(join(TARGET, APPNAME, rel, dir)))
    for file in files:
        n, e = os.path.splitext(file)
        if e != '.py': continue
        if n.startswith('test'): continue
        newname = n + '.pyc'
        py_compile.compile(join(root, file), abspath(join(TARGET, APPNAME, rel, newname)))


WD = os.path.abspath(TARGET)
os.chdir(WD)
print("CWD:", os.getcwd())
LIBDIR = 'lib'
DLLDIR = 'windll'
os.mkdir(LIBDIR)
os.mkdir(DLLDIR)
os.mkdir('plugins')

os.replace(join(WD, 'tkinterweb'), join(LIBDIR, 'tkinterweb'))

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
