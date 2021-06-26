from imports import *


FONTSIZEOPTIONS = (5, 8, 10, 11, 12, 16, 20, 24, 32)
IMAGETRESHHOLD = 5 * 1024 * 1024  # 10MB
# TAG2CONFIG = {
#     'fontsize': r'fontsize-(?P<value>\d)',
# }
# TAG2CONFIG: Dict[str, re.Pattern] = {key: re.compile(value) for key, value in TAG2CONFIG.items()}
DEFAULT_TAGS = {
    'bold': {

    },
    'italic': {

    },
    'underline': {
        'underline': True
    },
    'hyperlink': {

    }
}


class TextImage(tk.Label):
    pass


class TextEditor(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        top = tk.Frame(self)

        self.fsize = tk.IntVar(self, value=12)
        self.fsizew = tk.OptionMenu(top, self.fsize, *FONTSIZEOPTIONS)
        self.fsizew.grid(row=0, column=0, sticky=NSEW)
        self.b_bold = tk.Button(top, width=3, text="B", command=lambda: self.cmd_add_remove_tag('bold'))
        self.b_bold.grid(row=0, column=1, sticky=NSEW, padx=1, pady=1)
        self.b_italic = tk.Button(top, width=3, text="I", command=lambda: self.cmd_add_remove_tag('italic'))
        self.b_italic.grid(row=0, column=2, sticky=NSEW, padx=1, pady=1)
        self.b_underline = tk.Button(top, width=3, text="U", command=lambda: self.cmd_add_remove_tag('underline'))
        self.b_underline.grid(row=0, column=3, sticky=NSEW, padx=1, pady=1)
        tk.Button(top, width=3, text="🖼", command=self.cmd_image, font="20").grid(row=0, column=4, sticky=NSEW, padx=1, pady=1)

        self.text = text = tk.Text(self)
        scroll = tk.Scrollbar(self, command=text.yview)
        text.configure(yscrollcommand=scroll.set)

        for tagname, tagconfig in DEFAULT_TAGS.items():
            self.text.tag_configure(tagname, **tagconfig)

        # self.text.bind('<Control-t>', lambda e: self.text.tag_add('bluefg', 'sel.first', 'sel.last'))
        # self.text.tag_configure('bluefg', foreground='blue')

        bottom = tk.Frame(self)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        top.grid(row=0, column=0, columnspan=2, sticky=EW)
        text.grid(row=1, column=0, sticky=NSEW)
        scroll.grid(row=1, column=1, sticky=NS)
        bottom.grid(row=2, column=0, columnspan=2, sticky=EW)

        self.images: Dict[str, Dict[str, Union[str, Tuple[int, int], bytes]]] = {}
        self.tkimages: Set[tk.PhotoImage] = set()
        r"""
        self.images = {
            'a1040ec8-e3a2-4ee0-b9cb-b63c10787542': {
                'filename': 'Python.png',
                'size': [200, 200],
                'data': b'...'
            },
            ...
        }
        """

    def save(self, fp: Union[AnyStr, io.BytesIO]) -> None:
        # .dump keys: text, mark, tagon, tagoff, image, and window
        def callback(key, value, index):
            pickle.dump((key, value, index), fp)
            if key == 'tagoff':
                conf = self.text.tag_configure(value)
                pickle.dump({k: v[-1] for k, v in conf.items() if v[-1]}, fp)
            elif key == 'image':
                imgdata: Dict[str, Union[str, Tuple[int, int], bytes]] = self.images[value]
                pickle.dump(imgdata, fp)

        self.text.dump(1.0, 'end', callback)

    def load(self, fp: Union[AnyStr, io.BytesIO]) -> None:
        try:
            text = self.text
            tagopen = {}
            while True:
                key, value, index = pickle.load(fp)
                print((key, value, index))
                if key == 'text':
                    text.insert(index, value)
                elif key == 'tagon':
                    tagopen[value] = index
                elif key == 'tagoff':
                    text.tag_add(value, tagopen.pop(value), index)
                    got = pickle.load(fp)
                    if value not in DEFAULT_TAGS:  # prevent override from default-tags
                        text.tag_configure(value, **got)
                elif key == 'mark':
                    continue
                    # text.mark_set(value, index)
                elif key == 'image':
                    imgdata: Dict[str, Union[str, Tuple[int, int], bytes]] = pickle.load(fp)
                    self.images[value] = imgdata
                    self.insert_image(value, index)
                elif key == 'window':
                    pass
                else:
                    raise KeyError(key)
        except EOFError:
            self.text.delete('end-1c')  # remove last \n that required is for insert but not for anything else

    def cmd_add_remove_tag(self, tag: str):
        text = self.text
        sel_range = text.tag_ranges('sel')
        if sel_range:
            if tag in text.tag_names(sel_range[0]):
                text.tag_remove(tag, *sel_range)
            else:
                text.tag_add(tag, *sel_range)
        else:
            if tag in text.tag_names('insert'):
                text.tag_remove(tag, 'insert')
            else:
                text.tag_add(tag, 'insert')

    def insert_image(self, name, index):
        data = self.images[name]
        stream = io.BytesIO(data['data'])
        stream.name = data['filename']
        image: Image.Image = Image.open(stream)
        imagetk = ImageTk.PhotoImage(image)
        self.tkimages.add(imagetk)
        self.text.image_create(index, image=imagetk, name=name)

    def cmd_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", '*.png *.jpg *.gif'), ("All Files", '*.*')]
        )
        if not path: return
        filename = os.path.basename(path)

        stream = io.BytesIO()
        stream.name = filename  # for the .save of PIL
        file = open(path, 'rb')
        img: Image.Image = Image.open(file)
        config = {}
        filesize = os.path.getsize(path)
        if filesize > IMAGETRESHHOLD:
            answer = mb.askyesno('reducing?', 'The image size is to big. Should it be reduced to improve editor performance?')
            if answer is None: return
            elif answer:
                config['quality'] = 85
                config['optimize'] = True
        img.save(stream, **config)
        file.close()

        uid = str(uuid.uuid4())
        stream.seek(0)
        self.images[uid] = {
            'filename': filename,
            'size': img.size,
            'rotation': 0,
            'data': stream.read()
        }
        print(f"filesize reduced from {filesize // 1024} to {len(self.images[uid]['data']) // 1024}")
        self.insert_image(uid, index=INSERT)
