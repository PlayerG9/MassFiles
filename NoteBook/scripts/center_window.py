from screeninfo import get_monitors, Monitor
import typing as T
import tkinter


def center_window(window: T.Union['tkinter.Tk', 'tkinter.Toplevel'], width: T.Union[int, float] = None, height: T.Union[int, float] = None, screen0=False):
    if not hasattr(window, 'geometry'): raise ValueError('invalid window')

    # width, height = width or window.winfo_reqwidth(), height or window.winfo_reqheight()
    mousex, mousey = window.winfo_pointerxy()

    if screen0: boundy = None
    else: boundy = find_screen(mousex, mousey)

    if boundy is None: boundy = 0, window.winfo_screenwidth(), 0, window.winfo_screenheight()

    l, r, t, b = boundy
    w, h = r - l, b - t

    if width is None: width = window.winfo_reqwidth()
    if height is None: height = window.winfo_reqheight()
    # if width is None: width = window.winfo_width()
    # if height is None: height = window.winfo_height()
    # print([width, height])
    if 0.0 <= width <= 1.0: width = width * w
    if 0.0 <= height <= 1.0: height = height * h
    # print([width, height])

    # newGeometry = '{:.0f}x{:.0f}+{:.0f}+{:.0f}'.format(
    #     width, height,
    #     l + w / 2 - width / 2,
    #     t + h / 2 - height / 2,
    # )
    newGeometry = '{:.0f}x{:.0f}+{:.0f}+{:.0f}'.format(
        width, height,
        l + w / 2 - width / 2,
        t + h / 2 - height / 2,
    )
    # print(boundy, [w, h], [w / 2, h/2], [width / 2, height/2], newGeometry)
    # print([l, w, w/2, width, width/2])

    window.geometry(newGeometry)


def find_screen(x: int, y: int) -> T.Tuple[int, int, int, int]:
    for m in get_monitors():
        m: Monitor
        l, r, t, b = m.x, m.x + m.width, m.y, m.y + m.height
        # print([l, r, t, b], [x, y])
        if l < x < r and t < y < b:
            # print("Ja")
            return l, r, t, b
    return None
