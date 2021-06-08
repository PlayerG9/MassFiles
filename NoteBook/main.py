r"""
File-Structure
file.zip
+ images
| + image.png
+ files
| + hello_world.tktxt
| + hello_world
| | + hello_world_child.tktxt
+ config
| + settings.json

file.tktxt

"""
from imports import *
from editors.text import TextEditor
from filehandler import FileHandler


if not sys.argv:
    raise EnvironmentError("invalid sys.argv")
elif len(sys.argv) < 2:
    sys.argv.append("")


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.withdraw()

        txt = TextEditor(self)
        txt.pack(fill=BOTH, expand=1)

    def load(self) -> None:
        path = sys.argv[1]
        if not zf.is_zipfile(path):
            config = dict(
                defaultextension='.nb',
                filetypes=[('MassFile', 'nb'), ('All Filetypes', '*.*')]
            )
            answer = messages.askSomething("Invalid path", "Please select to continue", ['New', 'Open', 'Cancel'], cancel=2)
            if answer == 2: raise SilentError()
            elif answer == 1: path = filedialog.askopenfilename(**config)
            elif answer == 0: path = filedialog.asksaveasfilename(**config)
            else: raise ValueError('invalid selection')
            if not path: raise SilentError()
        if not os.path.exists(path):
            file = FileHandler.new(path)
        else:
            file = FileHandler(path)

    def run(self) -> None:
        # self.deiconify()
        self.mainloop()

    def report_callback_exception(self, exctype: type, exception: Exception, traceback: tb.TracebackException) -> None:
        if isinstance(exception, (SilentError,)): return
        mb.showerror(
            title=exctype,
            message='\n'.join(tb.format_exception(exctype, exception, traceback))
        )

    def debug(self):
        raise RuntimeError("Test")


def main():
    try:
        app = Application()  # build
        app.load()
    except SilentError: pass  # stop programm
    else: app.run()  # run programm


if __name__ == '__main__':
    main()
