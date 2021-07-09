from imports import *


class SettingWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.transient(self.master)
        center_window(self, 0.5, 0.5)

        self.grab_set()
