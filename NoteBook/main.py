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


if not sys.argv:
    raise EnvironmentError("invalid sys.argv")
elif len(sys.argv) < 2:
    sys.argv.append('./project.nb')


class ResourceManager:
    def __init__(self):
        pass


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        if not zipfile.is_zipfile(sys.argv[1]):
            mb.showerror("Invalid file")
            raise SilentError()

        txt = TextEditor(self)
        txt.pack(fill=BOTH, expand=1)

    def load(self):
        pass

    def run(self):
        self.after(1000, self.debug)
        self.mainloop()

    def report_callback_exception(self, exctype: type, exception: Exception, traceback: Exception.__traceback__):
        if isinstance(exception, (SilentError,)): return
        mb.showerror(
            title=exctype,
            message='\n'.join(tb.format_exception(exctype, exception, traceback))
        )

    def debug(self):
        raise RuntimeError("Test")


def main():
    try: app = Application()  # build
    except SilentError: pass  # stop programm
    else: app.run()  # run programm


if __name__ == '__main__':
    main()
