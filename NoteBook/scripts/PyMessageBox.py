r"""
PyMessageBox is a library independent (small) Module to give the user output
Copyright (c) 2021 PlayerG9. All rights reserved.

todo: TaskDialog
"""
import ctypes

__author__ = 'PlayerG9'
__version__ = '0.1'

__all__ = [
    'MessageBox',
    'EventMessageBox'
]

_msg = ctypes.windll.user32.MessageBoxW


_parseback = {
    1: 'OK',
    2: 'CANCEL',
    3: 'CANCEL',
    4: 'RETRY',
    5: 'IGNORE',
    6: 'YES',
    7: 'NO',
    10: 'RETRY',
    11: 'CONTINUE'
}


OK = 0
OK_CANCEL = 1
CANCEL_RETRY_IGNORE = 2
YES_NO_CANCEL = 3
YES_NO = 4
RETRY_CANCEL = 5
CANCEL_RETRY_CONTINUE = 6

ERROR = 16
ASK = 32
PANIC = 48
INFO = 64

# INVALID-CODE = 0
# OK = 1
# CANCEL = 2
# CANCEL = 3
# RETRY = 4
# IGNORE = 5
# YES = 6
# NO = 7
# RETRY = 10
# CONTINUE = 11


def MessageBox(title: str, message: str, style: int):
    r"""
    from PyMessageBox import MessageBox, INFO, YES_NO
    MessageBox("Title", "Message", INFO | YES_NO)
    """
    got = _msg(None, message, title, style)
    if not got:
        raise ValueError('invalid message-style: {!r}'.format(style))
    return _parseback.get(got, None)  # None should not happen


def EventMessageBox(title: str, message: str, style: int, **callbacks):
    r"""
    from PyMessageBox import EventMessageBox, INFO, YES_NO
    
    def cb_yes():
    	print("I like you project")
    
    def cb_no():
    	print("I don't like your project")
    	
    EventMessageBox("Title", "Do you like my project", INFO | YES_NO, YES=cb_yes, NO=cb_no)
    """
    if any(not event.isupper() for event in callbacks.keys()):
        raise KeyError('event must be uppercase')
    callbacks = {e: cb for e, cb in callbacks.items()}

    got = MessageBox(title, message, style)

    if got not in callbacks:
        raise KeyError('missing event: {!r}'.format(got))

    return callbacks[got]()


if __name__ == '__main__':
    
    print(MessageBox("Test", "Test is ok", INFO | OK))
    
    EventMessageBox("Test", "Is it ok?", ASK | OK_CANCEL,
                    OK=lambda: print("Is OK"),
                    CANCEL=lambda: print("Cancel it"))
