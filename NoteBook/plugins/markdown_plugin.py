r"""
Plugin:
    Name: Markdown Editor
    Author: PlayerG9
    Version: 0.0.1
    Brief: Add a Editor for the .md extension
    Description:
        Adds an Editor for .md files

        Editor-Modes:
        - Edit
        - Edit and View
        - View
"""
from imports import *
from base import *


class MarkdownEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

    @staticmethod
    def cb_open(path: str) -> tk.Widget:
        w = MarkdownEditor()

        return w

    @staticmethod
    def cb_config(path: str):
        pass


register_filehandler('.md', MarkdownEditor)
