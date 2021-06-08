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

        self.protocol('WM_DELETE_WINDOW', self.on_close)

        # self.withdraw()

        self.txt = txt = TextEditor(self)
        txt.pack(fill=BOTH, expand=1)
        try:
            self.txt.load(open('./test.tktxt', 'rb'))
        except Exception as error:
            tb.print_exception(type(error), error, error.__traceback__)

    def on_close(self):
        self.txt.save(open('./test.tktxt', 'wb'))
        self.destroy()

    def load(self) -> None:
        path = sys.argv[1]
        make_new = False
        if not zf.is_zipfile(path):
            config = dict(
                defaultextension='.nb',
                filetypes=[('MassFile', 'nb'), ('All Filetypes', '*.*')]
            )
            answer = messages.askSomething("Invalid path", "Please select to continue", ['New', 'Open', 'Cancel'], cancel=2)
            if answer == 2: raise SilentError()
            elif answer == 1: path = filedialog.askopenfilename(**config)
            elif answer == 0:
                path = filedialog.asksaveasfilename(**config)
                make_new = True
            else: raise ValueError('invalid selection')
            if not path: raise SilentError()
        FileHandler.path = path
        if make_new:
            FileHandler.new()

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
