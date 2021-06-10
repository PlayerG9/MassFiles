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


FILEASKCONFIG = dict(
    defaultextension='.nb',
    filetypes=[('MassFile', 'nb'), ('All Filetypes', '*.*')]
)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.protocol('WM_DELETE_WINDOW', self.on_close)

        # self.withdraw()

        self.txt = txt = TextEditor(self)
        txt.place(relwidth=1.0, relheight=1.0)

        def tload():
            try:
                self.txt.load(open('files/test.tktxt', 'rb'))
            except Exception as error:
                tb.print_exception(type(error), error, error.__traceback__)

        EventHandler.register('<on-load>', tload)

    def on_close(self):
        self.txt.save(open('files/test.tktxt', 'wb'))
        self.destroy()

    def load(self) -> None:
        r"""
        """
        self.workdir()

        if FileHandler.test_restore():
            answer = mb.askyesno("", "Allready opened project found. Should it be restored?")
            if answer is None:
                raise SilentError()
            elif answer:
                FileHandler.restore()
            else:
                FileHandler.clearup()

        path = sys.argv[1]

        if path and zf.is_zipfile(path):
            FileHandler.path = path
            FileHandler.open()
        else:
            answer = messages.askSomething("", "Please select to continue", ['New', 'Open', 'Cancel'], cancel=2)
            if answer == 2: raise SilentError()
            elif answer == 1:
                path = filedialog.askopenfilename(**FILEASKCONFIG)
                if not path: raise SilentError()
                FileHandler.path = path
            elif answer == 0:
                path = filedialog.asksaveasfilename(**FILEASKCONFIG)
                if not path: raise SilentError()
                FileHandler.path = path
                FileHandler.new()
            else: raise ValueError('invalid selection')
            FileHandler.open()

        EventHandler.invoke('<on-load>')

    def debug(self):
        # pprint({k: v for k, v in os.environ.items()})
        pass

    def run(self) -> None:
        self.debug()
        # self.deiconify()
        self.mainloop()

    def report_callback_exception(self, exctype: type, exception: Exception, traceback: tb.TracebackException) -> None:
        if isinstance(exception, (SilentError,)): return
        mb.showerror(
            title=exctype,
            message='\n'.join(tb.format_exception(exctype, exception, traceback))
        )

    # @staticmethod
    # def initdir():
    #     if os.environ.get('PYCHARM_HOSTED'):
    #         wd = os.path.abspath('./')
    #     else:
    #         wd = os.path.dirname(sys.executable)
    #     os.chdir(wd)

    @staticmethod
    def workdir():
        if os.path.basename(os.path.abspath('./')) == 'workdir': return
        if os.environ.get('PYCHARM_HOSTED'):
            wd = os.path.abspath('./workdir')
        else:
            wd = os.path.join(os.path.dirname(sys.executable), 'workdir')
        os.chdir(wd)

    # def debug(self):
    #     raise RuntimeError("Test")


def main():
    try:
        app = Application()  # build
        app.load()
    except SilentError: pass  # stop programm
    else: app.run()  # run programm


if __name__ == '__main__':
    main()
