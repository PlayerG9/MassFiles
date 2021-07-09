r"""
tk.Frame based
"""
from imports import *
from interface.explorer import Explorer
from scripts import animationhandler


class Handler(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)

        self.detector = widgets.VerticalLabel(self, text='files', background='gray80')
        self.detector.grid(row=0, column=0, sticky=NS)

        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=1, sticky=NSEW)

        self.explorer = Explorer(self)

        self.anim = animationhandler.SlideAnimation(
            self.explorer, side=W, speed=0.3,
            height=self.winfo_height
        )

        self.detector.bind('<Enter>', lambda e: self.anim.slide_in())
        self.explorer.bind('<Leave>', lambda e: self.anim.slide_out())

        self.bind('<Configure>', self.resize_explorer)
        self.explorer.bind('<Configure>', self.resize_explorer)

    def resize_explorer(self, event):
        if not self.explorer.place_info(): return
        self.explorer.place(height=event.height)
