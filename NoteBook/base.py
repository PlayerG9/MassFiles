filehandler = {}


class RegisterError(Exception):
    pass


def register_filehandler(fileext: str, handler: callable, force=False):
    if fileext in filehandler and not force:
        raise RegisterError('{!r} is allready registered'.format(fileext))

    filehandler[fileext] = handler


def open2(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    from os.path import join, abspath
    import traceback as tb
    from CONSTANTS import APPDIR

    i = tb.walk_stack(None)
    frame = next(i)[0]
    package = frame.f_locals['__package__']
    basedir = join(APPDIR, package.replace('.', '\\'))
    file = abspath(join(basedir, file))

    return open(file, mode, buffering, encoding, errors, newline, closefd)
