import sys

from imports import *


class InvalidFile(Exception): pass
class BrokenFile(Exception): pass


class FileHandler:
    path: str

    def __init__(self):
        path = FileHandler.path
        if not zf.is_zipfile(path):
            raise InvalidFile(path)
        self._path = path
        self._file = zf.ZipFile(path, 'a', compression=zf.ZIP_DEFLATED)
        if self._file.testzip():
            raise BrokenFile(path)
        self._file.printdir(sys.stderr)

    @staticmethod
    def new() -> "FileHandler":
        path = FileHandler.path
        if os.path.isfile(path):
            raise FileExistsError(path)
        with zf.ZipFile(path, 'w') as file:
            for dirname in ('images/', 'files/', 'configs/'):
                file.writestr(dirname, '')
            # file.writestr('files/file a.txt', 'Erste Datei a')
            # file.writestr('files/file a/', '')
            # file.writestr('files/file a/unter b.txt', 'Unterdatei b')

    def image(self, name: AnyStr, mode='r'):
        return self._file.open('images/' + name, mode)

    def listdir(self, dirpath: AnyStr, pre='files/'):
        path = os.path.normpath(os.path.join(pre, dirpath))
        for filename in self._file.namelist():
            if os.path.dirname(filename.removesuffix('/')) != path: continue
            yield filename

    def file(self, name: AnyStr, mode='r'):
        return self._file.open('files/' + name, mode)

    def config(self, name: AnyStr, mode='r'):
        return self._file.open('configs/' + name, mode)
