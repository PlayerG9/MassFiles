import sys

from imports import *


class InvalidFile(Exception): pass
class BrokenFile(Exception): pass


class FileHandler:
    def __init__(self, path: Union[AnyStr]):
        if not zf.is_zipfile(path):
            raise InvalidFile(path)
        self._path = path
        self._file = zf.ZipFile(path, 'a', compression=zf.ZIP_DEFLATED)
        if self._file.testzip():
            raise BrokenFile(path)
        self._file.printdir(sys.stderr)

    @staticmethod
    def new(path: Union[AnyStr]) -> "FileHandler":
        if os.path.isfile(path):
            raise FileExistsError(path)
        with zf.ZipFile(path, 'w') as file:
            for dirname in ('images', 'files'):
                file.writestr(dirname, '')
        return FileHandler(path)

    @property
    def images(self):
        return self._file

    @property
    def files(self):
        return self._file

    @property
    def configs(self):
        return self._file
