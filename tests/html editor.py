r"""
<html>
  <head>
    <meta charset="utf-8">
    <style>
html {
  background-color: #123;
  color: abc;
}

code {

}
    </style>
</head>
    <body>
      <p>Pre-Text<br>
<code>codeblock
line 2</code><br>
After-text</p>
  </body>
</html>
"""
from imports import *
from interface.widgets import HtmlView


def cmd(_=None):
    view.load_html(text.get(1.0, END))


root = tk.Tk()

text = tk.Text()
text.pack(fill=Y, expand=1, side=LEFT)
text.bind('<KeyRelease>', cmd)

view = HtmlView(root)
view.pack(fill=Y, expand=1, side=RIGHT)

root.mainloop()
