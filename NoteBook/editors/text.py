from imports import *


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

    def save(self, fp: Union[AnyStr, io.BytesIO]) -> None:
        # .dump keys: text, mark, tagon, tagoff, image, and window
        pass

    def load(self, fp: Union[AnyStr, io.BytesIO]) -> None:
        pass
