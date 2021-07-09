r"""
Plugin:
    Name: Markdown Editor
    Author: PlayerG9
    Version: 0.0.1
    Brief: Add a Editor for the .md extension
    Description:
        Adds an Editor for .md files

        Editor-Modes:
        - Edit
        - Edit and View
        - View
"""
from imports import *
from base import *


with open2('shell.html', 'r') as shellfile:
    shell = shellfile.read()


# [//]: # ({"Data": true, "sub": {"dato": false}})
detectdata = re.compile(r'^\[//]: # \((?P<json>{.*})\)')

call_limit_delta = 0.2  # 0.5 seconds between key-release and rendering
cld = int(call_limit_delta * 1000)  # in milliseconds for tk.Widget.after()


class MarkdownEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.call_limit_time: float = 0

        self.topbar = frame = tk.Frame(self)
        self.topbar.grid(row=0, sticky=EW)
        frame.grid_columnconfigure(9, weight=1)

        btnfont = tkfont.Font(
            self,
            font=["Segoe UI", 15]
        )
        btnconf = {
            'font': btnfont,
            'padx': 0,
            'pady': 0
        }

        for i in range(4):
            frame.grid_columnconfigure(i, minsize=25)
        widgets.LabelButton(
            frame,
            text='𝗕',
            command=lambda: self.insert('**', '**'),
            **btnconf
        ).grid(row=0, column=0, sticky=NSEW)
        widgets.LabelButton(
            frame,
            text='𝑰',
            command=lambda: self.insert('~~', '~~'),
            **btnconf
        ).grid(row=0, column=1, sticky=NSEW)
        widgets.LabelButton(
            frame,
            text='⎁',
            command=lambda: self.insert('__', '__'),
            **btnconf
        ).grid(row=0, column=2, sticky=NSEW)
        widgets.LabelButton(
            frame,
            text='🄪',
            command=lambda: self.insert('`', '`'),
            **btnconf
        ).grid(row=0, column=3, sticky=NSEW)

        self.btn_editor = widgets.LabelButton(
            frame,
            text='🖹',
            command=lambda: self.set_viewmode(1),
            **btnconf
        )
        self.btn_editor_and_view = widgets.LabelButton(
            frame,
            text='🖻',
            command=lambda: self.set_viewmode(2),
            **btnconf
        )
        self.btn_view = widgets.LabelButton(
            frame,
            text='🖼',
            command=lambda: self.set_viewmode(3),
            **btnconf
        )

        self.pane = tk.PanedWindow(
            master=self,
            opaqueresize=True,  # maybe to False for performance
            orient=HORIZONTAL,
            sashwidth=10,  # for better grip
        )
        self.pane.grid(row=1, sticky=NSEW)

        self.btn_editor.grid(row=0, column=10)
        self.btn_editor_and_view.grid(row=0, column=11)
        self.btn_view.grid(row=0, column=12)

        self.editorframe = frame = tk.Frame(self)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        self.editor = tk.Text(
            master=frame,
            wrap=NONE,  # not None
        )
        xscroll = widgets.AutoScrollbar(frame, orient=HORIZONTAL, command=self.editor.xview)
        yscroll = widgets.AutoScrollbar(frame, orient=VERTICAL, command=self.editor.yview)
        self.editor.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        self.editor.grid(row=0, column=0, sticky=NSEW)
        xscroll.grid(row=1, column=0, sticky=EW)
        yscroll.grid(row=0, column=1, sticky=NS)

        self.view = widgets.HtmlView(self)

        self.editor.bind('<Key>', lambda e: self.render_call())

        # self.editor.grid(row=1, column=0, sticky=NSEW)
        # self.view.grid(row=1, column=1, sticky=NSEW)

    def load(self, text: str):
        data = {}
        m = detectdata.match(text)
        if m:
            try:
                data = json.loads(m.group('json'))
            except json.JSONDecodeError:
                pass

        self.set_viewmode(data.get('viewmode', 2))

        self.editor.delete(1.0, END)
        self.editor.insert(END, text)
        self.render()

        self.editor.focus_set()

    def render_call(self):
        # prevent too fast rendering
        self.call_limit_time = time.time() + call_limit_delta
        self.after(cld, self._render_call)

    def _render_call(self):
        if time.time() < self.call_limit_time: return
        self.render()

    def render(self):
        text = self.editor.get(1.0, END)

        html_raw = markdown.markdown(text)

        data = {
            'bg': self.editor.cget('background'),
            'fg': self.editor.cget('foreground')
        }

        style = r'''
html {
    background: %(bg)s;
    color: %(fg)s;
}

code {
    background: gray;
    color: black;
    padding: 1px;
}
''' % data

        html = shell.format(
            style=style,
            body=html_raw
        )

        # print(html)
        # print()
        self.view.load_html(html)

    def set_viewmode(self, mode: int):
        print("Set-Viewmode:", mode)
        self.pane.remove(self.editorframe)
        self.pane.remove(self.view)

        if mode == 1:
            self.btn_editor.configure(relief=RIDGE)
            self.btn_editor_and_view.configure(relief=FLAT)
            self.btn_view.configure(relief=FLAT)

            self.pane.add(self.editorframe)
        elif mode == 2:
            self.btn_editor.configure(relief=FLAT)
            self.btn_editor_and_view.configure(relief=RIDGE)
            self.btn_view.configure(relief=FLAT)

            self.pane.add(self.editorframe)
            self.pane.add(self.view)
        elif mode == 3:
            self.btn_editor.configure(relief=FLAT)
            self.btn_editor_and_view.configure(relief=FLAT)
            self.btn_view.configure(relief=RIDGE)

            self.pane.add(self.view)
        else:
            raise KeyError('invalid mode {}'.format(mode))

    def insert(self, before, after):
        pass


########################################################################################################################


class CallbackHandler:
    @staticmethod
    def cb_open(path: str) -> tk.Widget:
        w = MarkdownEditor()

        with open(path, 'r') as file:
            data = file.read()

        w.load(data)

        return w

    @staticmethod
    def cb_config(path: str):
        pass


register_filehandler('.md', CallbackHandler)
