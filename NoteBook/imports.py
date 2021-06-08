import tkinter as tk
from tkinter.constants import *
from tkinter import filedialog
from tkinter import messagebox as mb

import os
import sys
import traceback as tb

import zipfile as zf
import pickle
import io

from PIL import Image, ImageTk

from typing import Union, Tuple, Any, List, AnyStr

from scripts import messages


class SilentError(Exception):
    pass
