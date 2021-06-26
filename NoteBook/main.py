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
from filehandler import FileHandler
from interface import window_about

import base64


if not sys.argv:
    raise EnvironmentError("invalid sys.argv")
elif len(sys.argv) < 2:
    sys.argv.append("")


FILEASKCONFIG = dict(
    defaultextension='.nb',
    filetypes=[('MassFile', 'nb'), ('All Filetypes', '*.*')]
)


class Application(tkdnd.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()

        self.protocol('WM_DELETE_WINDOW', self.on_close)

        self.option_add('*Button.cursor', 'hand2')

        icodata = base64.standard_b64decode(PYIMAGEDATA)
        self.ico = tk.PhotoImage(master=self, data=icodata)
        self.wm_iconphoto(True, self.ico)

        self.initdir()

        self.plugins = {}
        self.load_plugins()

        self.build_menu()

        # self.withdraw()

        # self.txt = txt = TextEditor(self)
        # txt.place(relwidth=1.0, relheight=1.0)

        # def tload():
        #     try:
        #         self.txt.load(open('files/test.tktxt', 'rb'))
        #         self.txt.focus_set()
        #     except Exception as error:
        #         tb.print_exception(type(error), error, error.__traceback__)

        # EventHandler.register('<on-load>', tload)

    def load_plugins(self):
        import importlib
        PLUGINDIR = './plugins'
        for filename in os.listdir(PLUGINDIR):
            fname, fext = os.path.splitext(filename)
            if fext != '.py': continue
            if not fname.endswith('_plugin'): continue
            print("Import-Plugin:", fname)
            try:
                plugin = importlib.import_module(f'plugins.{fname}')
                self.plugins[fname] = plugin
                if hasattr(plugin, 'init'):
                    plugin.init(self)
            except Exception as exc:
                self.report_callback_exception(type(exc), exc, exc.__traceback__)

    def on_close(self):
        # self.txt.save(open('files/test.tktxt', 'wb'))
        self.destroy()

    def load(self) -> None:
        r"""
        """
        self.workdir()

        to_restore = FileHandler.test_restore()
        if to_restore:
            answer = mb.askyesno("", f"Allready opened project found.\n{to_restore}\n Should it be restored?")
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
        # raise Exception()
        pass

    def run(self) -> None:
        self.after(1000, self.debug)
        # self.deiconify()
        self.state('normal')
        self.mainloop()

    def report_callback_exception(self, exctype: type, exception: Exception, traceback: tb.TracebackException) -> None:
        if isinstance(exception, (SilentError,)): return
        mb.showerror(
            title=exctype,
            message='\n'.join(tb.format_exception(exctype, exception, traceback))
        )

    @staticmethod
    def initdir():
        wd = os.path.join(APPDIR, 'NoteBook')
        os.chdir(wd)

    @staticmethod
    def workdir():
        if os.path.basename(os.path.abspath('./')) == 'workdir': return
        if not os.path.exists(FILES):
            os.mkdir(FILES)
        os.chdir(FILES)

    def build_menu(self):
        menu = tk.Menu(self, tearoff=0)

        pm = tk.Menu(menu, tearoff=0)
        pm.add_command(label="Save")
        fme = tk.Menu(pm, tearoff=0, postcommand=lambda: print("Import"))
        pm.add_cascade(label="Import", command=lambda: print("Import"), menu=fme)
        fmi = tk.Menu(pm, tearoff=0, postcommand=lambda: print("Export"))
        pm.add_cascade(label="Export", command=lambda: print("Export"), menu=fmi)
        menu.add_cascade(label="Project", menu=pm)

        fm = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=fm)

        em = tk.Menu(menu, tearoff=0, postcommand=lambda: print("Edit"))
        menu.add_cascade(label="Edit", menu=em)

        wm = tk.Menu(menu, tearoff=0)
        wm.add_command(label="About", command=window_about.WAbout)
        menu.add_cascade(label="Window", menu=wm)

        self.configure(menu=menu)

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
