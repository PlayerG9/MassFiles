from imports import *
import shutil
import atexit


class InvalidFile(Exception): pass
class BrokenFile(Exception): pass


class FileHandler:
    path: str

    @staticmethod
    def test_restore() -> bool:
        if os.path.isfile('filepath'):
            with open('filepath', 'r') as file:
                return file.read()
        return ''

    @staticmethod
    def restore():
        p = getattr(FileHandler, 'path', None)  # save for later
        with open('filepath', 'r') as file:
            FileHandler.path = file.read()  # read old path
        FileHandler.close()  # save data and clear memory
        FileHandler.path = p  # restore dir

    @staticmethod
    def open():
        path = FileHandler.path
        if not zf.is_zipfile(path):
            raise InvalidFile(path)

        file = zf.ZipFile(path, 'r', compression=zf.ZIP_DEFLATED, compresslevel=9)
        if file.testzip():
            raise BrokenFile(path)
        file.printdir(sys.stderr)

        file.extractall('./')  # todo need to improved to extractmember + update-callback
        with open('./filepath', 'w') as file:
            file.write(path)

        atexit.register(FileHandler.close)

    @staticmethod
    def new() -> "FileHandler":
        path = FileHandler.path
        if os.path.isfile(path):
            raise FileExistsError(path)
        with zf.ZipFile(path, 'w') as file:
            for dirname in ('files/', 'configs/'):
                file.writestr(dirname, '')
            default_data = {
                'comment': '',
                'createtime': '',
                'author': os.environ.get('USERNAME', None)
            }
            file.writestr('project.json', json.dumps(default_data))

    @staticmethod
    def fileimport(source: str, dist: str):
        shutil.copy(source, dist)

    @staticmethod
    def save():
        path = FileHandler.path
        os.remove('./filepath')
        file = zf.ZipFile(path, 'w', compression=zf.ZIP_DEFLATED, compresslevel=9)
        start = os.path.abspath('./')
        for root, dirs, files in os.walk(start):
            for fname in files:
                fpath = os.path.join(root, fname)
                apath = os.path.relpath(fpath, start)
                file.write(fpath, apath)

    @staticmethod
    def clearup():
        shutil.rmtree('./', ignore_errors=True, onerror=lambda *a: tb.print_exception(*a))

    @staticmethod
    def close():
        FileHandler.save()
        FileHandler.clearup()
