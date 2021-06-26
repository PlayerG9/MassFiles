filehandler = {}


class RegisterError(Exception):
    pass


def register_filehandler(fileext: str, handler: callable, force=False):
    if fileext in filehandler and not force:
        raise RegisterError('{!r} is allready registered'.format(fileext))

    filehandler[fileext] = handler
