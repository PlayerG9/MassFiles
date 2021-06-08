from imports import *
from tkinter import simpledialog

r"""
class _askDialog(simpledialog.Dialog):
    def __init__(self, title, config):
        self.config = config

        self.parent = parent = master = tk._get_default_root('create dialog window')

        tk.Toplevel.__init__(self, master)

        self.withdraw()  # remain invisible for now
        # If the parent is not viewable, don't
        # make the child transient, or else it
        # would be opened withdrawn
        self.transient(master)

        if title:
            self.title(title)

        self.result = None

        body = tk.Frame(self)
        self.body(body)
        body.pack(padx=5, pady=5, fill=BOTH, expand=1)

        self.buttonbox()

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        if parent is not None:
            self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                      parent.winfo_rooty()+50))

        self.deiconify()  # become visible now

        self.focus_set()

        # wait for window to appear on screen before calling grab_set
        self.wait_visibility()
        self.grab_set()
        self.wait_window(self)

    def body(self, master):
        if self.config.get('message'):
            tk.Label(master, text=self.config['message']).place(relwidth=1.0, relheight=1.0)

    def buttonbox(self):
        frame = tk.Frame(self)
        frame.pack(fill=X)
        options = self.config['options']
        for index, text in enumerate(options):
            frame.grid_columnconfigure(index, weight=1)
            tk.Button(frame, text=text, command=lambda i=index: self._confirm(i)).grid(row=0, column=index, padx=5, pady=5, sticky=NSEW)

    def _confirm(self, index):
        self.result = self.config['options'][index]
        self.destroy()
"""


def askSomething(title: AnyStr=None, message: AnyStr = None, options: List[AnyStr] = None, **config):
    d = simpledialog.SimpleDialog(config.get('master', tk._default_root), message, options, title=title, **config)
    return d.go()
