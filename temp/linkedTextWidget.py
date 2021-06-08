import tkinter as tk

class TextPeer(tk.Text):
    """A peer of an existing text widget"""
    count = 0
    def __init__(self, master, cnf={}, **kw):
        TextPeer.count += 1
        parent = master.master
        peerName = "peer-{}".format(TextPeer.count)
        if str(parent) == ".":
            peerPath = ".{}".format(peerName)
        else:
            peerPath = "{}.{}".format(parent, peerName)

        # Create the peer
        master.tk.call(master, 'peer', 'create', peerPath, *self._options(cnf, kw))

        # Create the tkinter widget based on the peer
        # We can't call tk.Text.__init__ because it will try to
        # create a new text widget. Instead, we want to use
        # the peer widget that has already been created.
        tk.BaseWidget._setup(self, parent, {'name': peerName})


root = tk.Tk()

text1 = tk.Text(root, width=40, height=4, font=("Helvetica", 20))
text2 = tk.Text(root, width=40, height=4, background="pink", font=("Helvetica", 16))
text3 = TextPeer(text2, width=40, height=8, background="yellow", font=("Fixed", 12))

text1.pack(side="top", fill="both", expand=True)
text2.pack(side="top", fill="both", expand=True)
text3.pack(side="top", fill="both", expand=True)

print(text1)
print(text2)
print(text3)

text2.insert("end", (
    "Type in one, and the change will "
    "appear in the other."
))
root.mainloop()
