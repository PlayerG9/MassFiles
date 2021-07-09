import sys as __sys
import os as __os
from enum import Enum as __Enum

# if getattr(__sys, 'frozen', False):
#     APPDIR = __os.path.dirname(__sys.executable)
# else:
#     APPDIR = __os.path.dirname()

CODEDIR = __os.path.dirname(__file__)
if getattr(__sys, 'frozen', False):
    CODEDIR = __os.path.join(CODEDIR, 'NoteBook')

APPDIR = __os.path.abspath(__os.path.join(CODEDIR, '..'))

FILES = __os.path.join(APPDIR, 'workdir')

LANGUAGES = __os.path.join(APPDIR, 'languages')

# print(f"{CODEDIR=}\n{APPDIR=}\n{FILES=}")

PYICONDATA = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5+fkA9/f3APb29gD39/cA+fn5APX19QD29vYA+Pj4APb29gD09PQA+Pj4APf39wD09PQA9/f3APn5+QD29vYA9vb2APn5+QD39/cA9PT0APf39wD39/cA9PT0APb29gD4+PgA9vb2APX19QD5+fkA9/f3APb29gD4+PgA+fn5APj4+AD39/cA9vb2APf39wD4+PgA9vb2APb29gD39/cA9vb2APX19QD39/cA9/f3APb29gD39/cA+Pj4APb29gD29vYA+Pj4APf39wD29vYA9/f3APf39wD19fUA9vb2APf39wD29vYA9vb2APj4+AD39/cA9vb2APf39wD4+PgA9vb2APb29gD39/cA9vb2APb29gD39/cA9/f3APb29gD39/cA+Pj4APb29gD29vYA+Pj4APj4+ABx1fsLErr5Mxa5+jNv0/gL+Pj4APj4+AD29vYA9vb2APj4+AD39/cA9vb2APf39wD39/cA9vb2APb29gD39/cA9vb2APb29gD4+PgA9/f3APb29gD39/cA+Pj4APb29gD29vYA9/f3APb29gD29vYAK8b2CjO++WEQufixHLr47Qy5+P8Mufj/DLn4/wy5+P8auvjsEbr4sTS++GEvxPYK9vb2APb29gD39/cA9vb2APb29gD4+PgA9/f3APb29gD39/cA+Pj4APn5+QD4+PgA9vb2APj4+AD6+voA9fX1APb29gD4+PgA9vb2ACq5+isRufjrDLn4/wy5+P8Mufj/DLn4/wy5+P8Mufj/DLn4/wy5+P8Mufj/DLn4/xC6+Oslu/gr9vb2APj4+AD29vYA9fX1APr6+gD4+PgA9vb2APj4+AD5+fkA9fX1APb29gD39/cA9vb2APX19QD39/cA9/f3APb29gD39/cADLn4Zgy5+P8Mufj/DLn4/wy5+P8Mufj/DLn4/wy5+P8Mufj/DLn4/wy5+P8Mufj/DLn4/w24+Gb39/cA9vb2APf39wD39/cA9fX1APb29gD39/cA9vb2APX19QD29vYA9vb2APf39wD29vYA9vb2APf39wD39/cA9vb2APf39wAMufhmDLn4/wy5+P8Mufj/DLn4/wy5+P8Mufj/DLn4/wy5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Uv+9aFL/vWhS/56KpZkMufj/DLn4/wy5+P8Mufj/DLn4/zK++WH29vYA9/f3APj4+AD4+PgA9/f3APb29gDFd2wKvmlT671oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/noqlmQy5+P8Mufj/DLn4/wy5+P8RufjrKsb2Cvb29gD39/cA+Pj4APT09AD29vYA+Pj4APX19QC8aVUpvWhSZr1oUma9aFJmvWhSZr1oUnq9aFKZvWhSmb1oUpm9aFKZvWhSmb1oUpm9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+ueoR6DLn4Zgy5+GYMufhmDLn4Zim5/Cv29vYA+Pj4APX19QD09PQA9vb2APb29gD39/cA9vb2APb29gD39/cA9/f3APb29gD39/cAvWhSZr1oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oU2b39/cA9vb2APf39wD39/cA9vb2APb29gD39/cA9vb2APb29gD4+PgA9/f3APb29gD39/cA+Pj4APb29gD29vYA9/f3APb29gC9aFJmvWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhTZvb29gD39/cA9vb2APb29gD4+PgA9/f3APb29gD39/cA+Pj4APb29gD29vYA9/f3APb29gD29vYA9/f3APf39wD29vYA9/f3AL1oUma9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFNm9/f3APb29gD39/cA9/f3APb29gD29vYA9/f3APb29gD29vYA9vb2APb29gD39/cA9vb2APX19QD39/cA9/f3APb29gD39/cAvWhSZr1oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oU2b39/cA9vb2APf39wD39/cA9fX1APb29gD39/cA9vb2APb29gD5+fkA+Pj4APb29gD4+PgA+vr6APX19QD29vYA+Pj4APb29gC8aVUpvWlT671oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aFL/vWhS/71oUv+9aVPrvmpVKfb29gD4+PgA9vb2APX19QD6+voA+Pj4APb29gD4+PgA+fn5APj4+AD39/cA9vb2APf39wD4+PgA9vb2APb29gD39/cA9vb2APX19QDCeGwKwXNfX75pU7G9aFLovWhS/71oUv+9aFL/vWhS/71oUui9aVOxwHFeXMB6Zgr29vYA9vb2APf39wD29vYA9vb2APj4+AD39/cA9vb2APf39wD4+PgA9vb2APb29gD39/cA9vb2APb29gD39/cA9/f3APb29gD39/cA+Pj4APb29gD29vYA+Pj4APj4+ADaopULvWtVM71pVTPZo5kL+Pj4APj4+AD29vYA9vb2APj4+AD39/cA9vb2APf39wD39/cA9vb2APb29gD39/cA9vb2APb29gD4+PgA9/f3APb29gD39/cA+Pj4APb29gD29vYA9/f3APb29gD29vYA9/f3APf39wD29vYA9/f3APj4+AD29vYA9vb2APj4+AD39/cA9vb2APf39wD39/cA9vb2APb29gD39/cA9vb2APb29gD4+PgA9/f3APb29gD39/cA+Pj4APn5+QD4+PgA9vb2APj4+AD5+fkA9vb2APb29gD4+PgA9vb2APT09AD4+PgA+Pj4APT09AD39/cA+fn5APb29gD29vYA+fn5APf39wD09PQA9/f3APj4+AD09PQA9vb2APj4+AD29vYA9fX1APn5+QD4+PgA9vb2APj4+AD5+fkA/////////////D///8AD//+AAf//gAH//4AB//+AAf//gAH/8AAAD+AAAAfgAAAH4AAAB+AAAAfAAAADwAAAA8AAAAPAAAAD4AAAB+AAAAfgAAAH4AAAB/AAAA//gAH//4AB//+AAf//gAH//4AB///AA////D////////////8='
PYIMAGEDATA = b'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'


class TYPES(__Enum):
    EXPLORER = 1
    EDITOR = 2
    WINDOW = 3
