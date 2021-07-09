import tkinter as tk
from tkinter.constants import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.scrolledtext import ScrolledText as tkScrolledText
from tkinter import font as tkfont
from tkinter import ttk

import tkinterdnd2 as tkdnd
from tkinterweb import htmlwidgets as tkweb

import markdown
import screeninfo

import os
import sys
import traceback as tb
from pprint import pprint

import zipfile as zf
import pickle
import io
import uuid
import json

from PIL import Image, ImageTk, ImageDraw, ImageFont

from typing import Union, Tuple, Dict, List, Set, AnyStr, Any

from datetime import datetime
import time

import re

from _thread import start_new_thread

from scripts import messages
from scripts.eventhandler import EventHandler
from scripts import animationhandler
from filehandler import FileHandler
from CONSTANTS import *
from scripts.languagesupport import language

from scripts import PyMessageBox
from scripts.center_window import center_window

from interface import widgets


pprint({k: v for k, v in os.environ.items()})


class SilentError(Exception):
    pass


__nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')


def __surrogatepair(match):
    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (
        chr(int.from_bytes(encoded[:2], 'little')) +
        chr(int.from_bytes(encoded[2:], 'little')))


def text2tk(text: str) -> str:
    return __nonbmp.sub(__surrogatepair, text)
