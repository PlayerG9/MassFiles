from imports import *


class AutoScrollbar(tk.Scrollbar):
    """Scrollbar that hides itself when not needed."""

    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
        super().set(lo, hi)

    def pack(self, **kw):
        raise tk.TclError("cannot use pack with this widget")

    def place(self, **kw):
        raise tk.TclError("cannot use place with this widget")


class LabelButton(tk.Label):
    """Label converted to Button because labels are smaller"""

    def __init__(self, master=None, cnf=None, **kwargs):
        kw = dict()  # default-config
        kw.update(kwargs)
        self.__cmd = kw.pop('command', None)
        super().__init__(master, cnf or {}, **kw)

        self.__relief = None

        self.bind('<Button-1>', self._btn_down)
        self.bind('<ButtonRelease-1>', self._btn_up)

    def _btn_down(self, _):
        self.__relief = self['relief']
        self.configure(relief=SUNKEN)

    def _btn_up(self, event):
        self.config(relief=self.__relief)
        self.__relief = None
        if not (0 <= event.x <= self.winfo_width() and 0 <= event.y <= self.winfo_height()):  # check if mouse still over "button"
            return
        if self.__cmd:
            self.__cmd()
