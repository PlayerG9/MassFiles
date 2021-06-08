from tkinter import *
import pickle


root = Tk()

t = Text()
t.pack(fill=BOTH, expand=1)
t.focus_set()

img = PhotoImage(file='./test.gif')
imgs = set()


t.bind('<Control-i>', lambda e: t.image_create('insert', image=img))


def loader():
    print(img)
    try:
        with open('./test.tktxt', 'rb') as file:
            while True:
                key, value, index = pickle.load(file)
                print((key, value, index))
                if key == 'mark':
                    t.mark_set(value, index)
                elif key == 'text':
                    t.insert(index, value)
                elif key == 'image':
                    newimg = PhotoImage(name=value.split('#')[0])
                    imgs.add(newimg)
                    t.image_create(index, image=newimg)
    except Exception as error:
        print([type(error), error])
    print(t.image_names())


class Dumper(object):
    file: open

    def __init__(self):
        print(imgs)

    def __enter__(self):
        print("Enter")
        self.file = open('./test.tktxt', 'wb')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        print([exc_type, exc_val, exc_tb])
        del self.file

    def call(self, *args):
        print(args)
        pickle.dump(args, self.file)
        if args[0] == 'image':
            print(t.image_configure(args[2]))


def show():
    d = Dumper()
    with d:
        t.dump(1.0, 'end-1c', d.call)
    root.destroy()


loader()
root.protocol('WM_DELETE_WINDOW', show)


root.mainloop()
