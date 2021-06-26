import importlib
import ctypes
import traceback
import sys
import os
sys.path.append(os.path.abspath('./NoteBook'))
try:
    import NoteBook.imports  # to properly load all libraries to the .exe
    app = importlib.import_module('NoteBook.main')  # no normal import to have the files extern
    app.main()
except Exception as exc:
    MessageBoxW = ctypes.windll.user32.MessageBoxW
    MessageBoxW(None, '\n'.join(traceback.format_exception(type(exc), exc, exc.__traceback__)), "Script crashed", 16)
