from imports import *
import base64


TEXT = r"""
Editor to manage a complex Project

Copyright (c) 2021 PlayerG9
""".strip()


class WAbout(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.transient(self.master)

        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry('{:.0f}x{:.0f}+{:.0f}+{:.0f}'.format(
            sw / 4, sh / 4, sw / 8 * 3, sh / 8 * 3
        ))
        self.update_idletasks()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        imgdata = base64.standard_b64decode(PYIMAGEDATA)
        self.img = tk.PhotoImage(master=self, data=imgdata)

        imglabel = tk.Label(self, anchor=CENTER, image=self.img)
        imglabel.grid(row=0, column=0)

        ttk.Separator(self, orient=HORIZONTAL).grid(row=1, column=0, sticky=EW, padx=10, pady=5)

        tk.Message(
            self,
            text=TEXT,
            anchor=NW,
            width=self.winfo_width()
        ).grid(row=2, column=0, sticky=NSEW, padx=2)

        ttk.Button(self, text='Ok', width=10, command=self.destroy).grid(row=3, column=0, sticky=E, padx=5, pady=5)

        self.after(50, self.focus_set)
        self.grab_set()
