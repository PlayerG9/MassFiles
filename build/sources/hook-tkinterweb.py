"""pyinstaller hook file.

"""

from PyInstaller.utils.hooks import collect_data_files, eval_statement
import os


datas = collect_data_files('tkinterweb', include_py_files=True)
