from imports import *
from base import *


ON = '☑'
OFF = '☐'


def get_state(t: str):
    if t == ON: return True
    elif t == OFF: return False
    raise ValueError()


filematch = re.compile(r'^(?P<state>[{}{}]) (?P<text>.+)$'.format(ON, OFF), re.MULTILINE)


class CheckListEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        head = tk.Frame(self, relief=RIDGE, bd=2)
        head.grid(row=0, columnspan=2, sticky=EW)
        widgets.LabelButton(head, text='➕', command=self.new).grid(row=0, column=0, sticky=NSEW)

        self.canvas = tk.Canvas(self, takefocus=False, relief=FLAT)

        self.frame = frame = tk.Frame(self.canvas)
        self.canvas.create_window(0, 0, window=frame, anchor=NW, tags='base')

        self.canvas.bind('<Configure>', lambda e: self.reconfigure())
        frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        # self.frame.bind('<Configure>', lambda e: self.reconfigure())

        xscroll = widgets.AutoScrollbar(self, orient=HORIZONTAL, command=self.canvas.xview)
        yscroll = widgets.AutoScrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        self.canvas.grid(row=1, column=0, sticky=NSEW)
        xscroll.grid(row=2, column=0, sticky=EW)
        yscroll.grid(row=1, column=1, sticky=NS)

    def load(self, fp):
        if isinstance(fp, str):
            fp = open(fp, 'r', encoding='utf-16')

        content = fp.read()

        for match in filematch.finditer(content):
            w = CheckListItem(self.frame)
            w.load((get_state(match.group('state')), match.group('text')))
            w.pack(fill=X)

    def save(self, fp):
        if isinstance(fp, str):
            fp = open(fp, 'w', encoding='utf-16')

        for child in self.frame.winfo_children():
            state, text = child.save()

            fp.write('{} {}\n'.format(ON if state else OFF, text))

    def reconfigure(self):
        self.canvas.itemconfigure(
            'base',
            width=max(self.frame.winfo_reqwidth(), self.canvas.winfo_width()-5),
            height=max(self.frame.winfo_reqheight(), self.canvas.winfo_height()-5)
        )

    def new(self):
        w = CheckListItem(self.frame)
        w.pack(fill=X)
        w.cmd_edit()

    # def on_key(self, event):
    #     print(event)
    #     if not event.key.isprintable(): return
    #     w = CheckListItem(self.frame)
    #     w.key_init(event.key)
    #     w.pack(fill=X)


########################################################################################################################


class CheckListItem(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.__state = False

        self.box = widgets.LabelButton(self, relief=FLAT, command=self.trigger)
        self.text = tk.Label(self, anchor=W)
        self.text.bind('<Double-Button-1>', lambda e: self.cmd_edit())
        # self.edit = widgets.LabelButton(self, text='✎', command=self.cmd_edit)
        self.delete = widgets.LabelButton(self, relief=FLAT, text='🗑', command=self.cmd_delete)

        self.entry = tk.Entry(self)
        self.entry.bind('<FocusOut>', lambda e: self._update_text())
        self.entry.bind('<Return>', lambda e: self.focus_set())
        self.entry.bind('<Tab>', lambda e: self.focus_set())
        self.entry.grid(row=0, column=1, sticky=NSEW)  # set the grid
        self.entry.grid_remove()

        self.grid_columnconfigure(1, weight=1)
        self.box.grid(row=0, column=0, sticky=NSEW)
        self.text.grid(row=0, column=1, sticky=NSEW)
        # self.edit.grid(row=0, column=2, sticky=NSEW)
        self.delete.grid(row=0, column=3, sticky=NSEW)

        fontstring: str = self.text.cget('font')
        self.normal_Font = tkfont.Font(font=fontstring)
        self.strike_Font = tkfont.Font(font=fontstring)
        self.strike_Font.configure(overstrike=1)

        self._update()

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
        self._update()

    def load(self, data: Tuple[bool, str]):
        self.state = data[0]
        self.text['text'] = data[1]

    def save(self) -> Tuple[bool, str]:
        return self.state, self.text['text']

    def cmd_edit(self):
        self.entry.grid()
        self.entry.delete(0, END)
        self.entry.insert(END, self.text['text'])
        self.entry.selection_range(0, END)
        self.entry.focus_set()

    def cmd_delete(self):
        self.destroy()

    def trigger(self):
        self.state = not self.state

    def _update(self):
        if self.state:
            self.box['text'] = ON
            self.text['font'] = self.strike_Font
        else:
            self.box['text'] = OFF
            self.text['font'] = self.normal_Font

    def _update_text(self):
        self.entry.grid_remove()
        if not self.entry.get(): return
        self.text['text'] = self.entry.get()


########################################################################################################################


class CallbackHandler:
    @staticmethod
    def cb_open(path: str) -> tk.Widget:
        w = CheckListEditor()

        w.load(path)

        return w

    @staticmethod
    def cb_config(path: str):
        pass


register_filehandler('.cl', CallbackHandler)
