from imports import *


class Explorer(tk.Frame):
    TYPE: str = TYPES.EXPLORER

    def __init__(self, master=None):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        menu = tk.Frame(self)
        menu.grid(row=0, columnspan=2, sticky=EW)

        self.tree = ttk.Treeview(
            self,
            columns=['type', 'size'],
            selectmode='extended',  # browse for one | extended for multiple

        )
        self.tree.heading('#0', text='file')
        self.tree.heading('type', text='type')
        self.tree.heading('size', text='size')
        self.yscroll = tk.Scrollbar(self, orient=VERTICAL, command=self.tree.set)
        self.tree.configure(yscrollcommand=self.yscroll.set)

        self.tree.grid(row=1, column=0, sticky=NSEW)
        self.yscroll.grid(row=1, column=2, sticky=NS)

    def update_tree(self):
        for root, dirs, files in os.walk('./files'):
            pass

    def popup(self, event):
        menu = tk.Menu(self, tearoff=False)

        menu.add_command(label="TODO")

        menu.post(event.x_root, event.y_root)
