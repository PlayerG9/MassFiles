from tkinter import *
from tkinterweb.htmlwidgets import HtmlFrame
import markdown


def render():
    text = in_.get(1.0, END)
    md = markdown.markdown(
        text
    )
    out.load_html(
        md
    )


root = Tk()


in_ = Text(root)
in_.pack(fill=X)
in_.bind('<KeyRelease>', lambda e: render())
out = HtmlFrame(root, messages_enabled=False)
out.pack(fill=X)

root.mainloop()
