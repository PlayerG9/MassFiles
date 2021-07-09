r"""
; comment
# also comment

[group]
item        =Item Text
sub-group   ={
    subgroupitem    =Subgroup Itemtext
    another         =Another item in the sub-group
}
another-item        =Another item in the group

[another-group]
"""
from imports import *


MISSING = object()


class LanguageObject:
    def __init__(self, path: str):
        self.data = {}

        # print("="*50)
        # self.data.update(self._parse(path))
        # print("=" * 50)
        # raise

    def extend(self, path: str):
        self.data.update(self._parse(path))

    def reload(self, path: str):
        self.data.clear()
        self.data.update(self._parse(path))

    @staticmethod
    def _parse(path: str):
        with open(path, 'r', encoding='utf-16') as file:
            content = file.read()

        back = {}

        content = re.sub(
            pattern=r'^[#;].*\n',  # remove comments
            repl='',
            string=content,
            flags=re.MULTILINE
        )

        # groups = re.compile(
        #     pattern=r'\n\[(?P<name>.+)]\n(?P<content>[.]+)',
        #     flags=re.DEBUG
        # )
        groups = re.compile(
            pattern='\n\[.+]\n[.]*',
            flags=re.DEBUG
        )
        # \n(P<content>[.\n]*)(?:^\[.+\]$)?
        # (?:\n\[.+]\n|$)

        for group in groups.finditer(content):
            print(10 * "=")
            print(group)
            print(group.groupdict())
            print(10 * "=")

        print(content)

        return back

    def get(self, what: str, default=MISSING):
        pass

    def __call__(self, what: str, default=None):
        pass


language = LanguageObject(os.path.join(LANGUAGES, 'english.lang'))
