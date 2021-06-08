import tkinter as tk
from tkinter.constants import *
from tkinter import filedialog
from tkinter import messagebox as mb

import os
import sys
import traceback as tb

import zipfile
import pickle
import io

from PIL import Image, ImageTk

from typing import Union, Tuple, Any, List, AnyStr


class SilentError(Exception):
    pass
