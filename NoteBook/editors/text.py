from imports import *
import re


FONTSIZEOPTIONS = (5, 8, 10, 11, 12, 16, 20, 24, 32)
TAG2CONFIG = {
    'fontsize': r'fontsize-(?P<value>\d)',
}
TAG2CONFIG: Dict[str, re.Pattern] = {key: re.compile(value) for key, value in TAG2CONFIG.items()}


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
        tk.Button(top, text="B", command=self.cmd_bold).grid(row=0, column=1, sticky=NSEW)
        tk.Button(top, text="I", command=self.cmd_italic).grid(row=0, column=2, sticky=NSEW)
        tk.Button(top, text="U", command=self.cmd_underline).grid(row=0, column=3, sticky=NSEW)

        self.text = text = TextWidget(self)
        scroll = tk.Scrollbar(self, command=text.yview)
        text.configure(yscrollcommand=scroll.set)

        self.text.tag_configure('bold', )
        self.text.tag_configure('italic', )
        self.text.tag_configure('underline', underline=True)

        # self.text.bind('<Control-t>', lambda e: self.text.tag_add('bluefg', 'sel.first', 'sel.last'))
        # self.text.tag_configure('bluefg', foreground='blue')

        # for fontsize in FONTSIZEOPTIONS:
        #     pass

        bottom = tk.Frame(self)

        top.grid(row=0, column=0, columnspan=2, sticky=EW)
        text.grid(row=1, column=0, sticky=NSEW)
        scroll.grid(row=1, column=1, sticky=NS)
        bottom.grid(row=2, column=0, columnspan=2, sticky=EW)

    def save(self, fp: Union[AnyStr, io.BytesIO]) -> None:
        # .dump keys: text, mark, tagon, tagoff, image, and window
        def callback(key, value, index):
            pickle.dump((key, value, index), fp)
            if key == 'tagoff':
                conf = self.text.tag_configure(value)
                pickle.dump({k: v[-1] for k, v in conf.items() if v[-1]}, fp)

        self.text.dump(1.0, 'end', callback)

    def load(self, fp: Union[AnyStr, io.BytesIO]) -> None:
        try:
            text = self.text
            tagopen = {}
            while True:
                key, value, index = pickle.load(fp)
                print((key, value, index))
                if key == 'text':
                    text.insert(index, value)
                elif key == 'tagon':
                    tagopen[value] = index
                elif key == 'tagoff':
                    text.tag_add(value, tagopen.pop(value), index)
                    got = pickle.load(fp)
                    print(got)
                    text.tag_configure(value, **got)
                elif key == 'mark':
                    text.mark_set(value, index)
                elif key == 'image':
                    pass
                elif key == 'window':
                    pass
                else:
                    raise KeyError(key)
        except EOFError:
            self.text.delete('end-1c')  # remove last \n that required is for insert but not for anything else

    def cmd_bold(self):
        pass

    def cmd_italic(self):
        pass

    def cmd_underline(self):
        text = self.text
        sel_range = text.tag_ranges('sel')
        if sel_range:
            if 'underline' in text.tag_names(sel_range[0]):
                text.tag_remove('underline', *sel_range)
            else:
                text.tag_add('underline', *sel_range)
        else:
            if 'underline' in text.tag_names('insert'):
                text.tag_remove('underline', 'insert')
            else:
                text.tag_add('underline', 'insert')
