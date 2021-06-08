r"""
File-Structure
file.zip
+ images
| + image.png
+ files
| + hello_world.tktxt
| + hello_world
| | + hello_world_child.tktxt
+ config
| + settings.json

file.tktxt

"""

import tkinter as tk
from tkinter.constants import *
from tkinter import filedialog
from tkinter import messagebox as mb
# from tkinter import scrolledtext

import os
import sys

import zipfile
import pickle

from PIL import Image, ImageTk


FONTSIZEOPTIONS = (5, 8, 10, 11, 12, 16, 20, 24, 32)


class TextWidget(tk.Text):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class TextEditor(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        top = tk.Frame(self)

        self.fsize = tk.IntVar(self, value=12)
        self.fsizew = tk.OptionMenu(top, self.fsize, *FONTSIZEOPTIONS)
        self.fsizew.grid(row=0, column=0, sticky=NSEW)

        text = TextWidget(self)
        scroll = tk.Scrollbar(self, command=text.yview)
        text.configure(yscrollcommand=scroll.set)

        bottom = tk.Frame(self)

        top.grid(row=0, column=0, columnspan=2, sticky=EW)
        text.grid(row=1, column=0, sticky=NSEW)
        scroll.grid(row=1, column=1, sticky=NS)
        bottom.grid(row=2, column=0, columnspan=2, sticky=EW)

    def save(self, fp):
        pass

    def load(self, fp):
        pass


class ImageEditor(tk.Frame):
    pass


class ResourceManager:
    def __init__(self):
        pass


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        txt = TextEditor(self)
        txt.pack(fill=BOTH, expand=1)

    def load(self):
        pass

    def run(self):
        self.mainloop()

    def report_callback_exception(self, exc, val, tb):
        pass


def main():
    app = Application()
    app.load()
    app.run()


if __name__ == '__main__':
    main()
