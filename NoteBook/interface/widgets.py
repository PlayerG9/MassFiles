from imports import *
import webbrowser


########################################################################################################################
# AutoScrollbar
########################################################################################################################


class AutoScrollbar(tk.Scrollbar):
    """Scrollbar that hides itself when not needed."""

    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
        super().set(lo, hi)

    def pack(self, **kw):
        raise tk.TclError("cannot use pack with this widget")

    def place(self, **kw):
        raise tk.TclError("cannot use place with this widget")


########################################################################################################################
# LabelButton
########################################################################################################################


class LabelButton(tk.Label):
    """Label converted to Button because labels are smaller"""

    def __init__(self, master=None, cnf=None, **kwargs):
        kw = dict(relief=RAISED)  # default-config
        kw.update(kwargs)
        self.__cmd = kw.pop('command', None)
        super().__init__(master, cnf or {}, **kw)

        self.__relief = None

        self.bind('<Button-1>', self._btn_down)
        self.bind('<ButtonRelease-1>', self._btn_up)

    def _btn_down(self, _):
        self.__relief = self['relief']
        self.configure(relief=SUNKEN)

    def _btn_up(self, event):
        self.config(relief=self.__relief)
        self.__relief = None
        if not (0 <= event.x <= self.winfo_width() and 0 <= event.y <= self.winfo_height()):  # check if mouse still over "button"
            return
        if self.__cmd:
            self.__cmd()


########################################################################################################################
# VerticalLabel
########################################################################################################################


class VerticalLabel(tk.Label):
    ROTATED = 'rotated'
    LINE = 'line'

    def __init__(self, master=None, **kwargs):
        # todo add image option
        text = kwargs.pop('text', None)
        style = kwargs.pop('style', self.ROTATED)
        super().__init__(master, **kwargs)
        self.__text = text
        self.__style = style
        self.__image: tk.PhotoImage = None
        self._render_text()

    def configure(self, cnf=None, **kw):
        if 'text' in kw:
            self.__text = kw.pop('text')
        if 'style' in kw:
            self.__style = kw.pop('style')
        super().configure(cnf, **kw)

    def __getitem__(self, item):
        if item == 'text':
            return self.__text
        if item == 'style':
            return self.__style
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if key == 'text':
            self.__text = value
        elif key == 'style':
            self.__style = value
        else:
            super().__setitem__(key, value)
        self._render_text()

    def _render_text(self):
        if self.__style == self.LINE:
            super().configure(text='\n'.join(self.__text))
        else:
            fontdata = self.__get_font()

            # convert font-name
            fontname: str = '%s.ttf' % fontdata['family'].lower().replace(' ', '')
            # font = ImageFont.truetype('segoeui.ttf', size=fontdata['size'])

            # load PIL-font
            font = ImageFont.truetype(fontname, size=fontdata['size'])
            size = font.getbbox(self.__text)[2:4]  # measure font-size
            img = Image.new('RGBA', size)  # create image according to size
            draw = ImageDraw.Draw(img)

            color = self.__get_color('foreground')

            draw.text((0, 0), text=self.__text, fill=color, font=font)

            img = img.rotate(angle=90, resample=Image.ANTIALIAS, expand=True)

            self.__image = ImageTk.PhotoImage(img)
            super().configure(image=self.__image)

    def __get_font(self) -> dict:
        fontstr = self.cget('font')
        font = tkfont.Font(root=self, font=fontstr)
        back = font.config()
        del font
        return back

    def __get_color(self, key) -> str:
        rgb = self.winfo_rgb(self.cget(key))
        r, g, b = [x >> 8 for x in rgb]
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)


########################################################################################################################
# HtmlView
########################################################################################################################


class HtmlView(tkweb.HtmlFrame):
    def __init__(self, master, **kwargs):
        kwargs.setdefault('messages_enabled', False)
        kwargs.setdefault('horizontal_scrollbar', 'auto')
        super().__init__(master, **kwargs)
        self.on_link_click(self.on_link)

    @staticmethod
    def on_link(url: str):
        webbrowser.open(url, autoraise=True)
