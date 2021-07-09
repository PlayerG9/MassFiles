from imports import *


########################################################################################################################
# SlideAnimation
########################################################################################################################


class SlideAnimation:
    INTERVAL = 10  # ms between .after() calls

    def __init__(self, widget: tk.Widget, side: Union[N, E, S, W], speed: int = 0.5, width=None, height=None):
        if side not in 'nesw': raise ValueError('invalid side {}'.format(side))
        self.widget = widget
        self.side = side
        self.speed = speed
        self.width = width
        self.height = height
        self.units = speed * 1000 / self.INTERVAL

        self.stop = tk.BooleanVar(widget, value=False)
        self.playing = tk.BooleanVar(widget, value=False)

    def slide_in(self):
        w = self.widget
        if self.playing.get():  # is playing?
            self.stop.set(True)  # set stop-var
            w.wait_variable(self.stop)  # wait until stop-var is set to False

        self.playing.set(True)  # set playing

        if callable(self.width): ww = self.width()
        elif self.width: ww = self.width
        else: ww = w.winfo_reqwidth()
        if callable(self.height): wh = self.height()
        elif self.height: wh = self.height
        else: wh = w.winfo_reqheight()

        mw = w.master.winfo_width()
        mh = w.master.winfo_height()
        print([ww, wh, mw, mh])

        w.place(width=ww, height=wh)

        side = self.side
        if side == N:
            w.place(x=0, y=-wh)
            delta = wh / self.units
            w.after(self.INTERVAL, lambda: self._cb_move(
                setfunc=lambda: w.place(y=w.winfo_y() + delta),
                testfunc=lambda: w.winfo_y() < 0
            ))
        elif side == E:
            w.place(x=mw, y=0)
            delta = ww / self.units
            w.after(self.INTERVAL, lambda: self._cb_move(
                setfunc=lambda: w.place(x=w.winfo_x() - delta),
                testfunc=lambda: w.winfo_x() > mw - ww
            ))
        elif side == S:
            w.place(x=0, y=mh)
            delta = wh / self.units
            w.after(self.INTERVAL, lambda: self._cb_move(
                setfunc=lambda: w.place(y=w.winfo_y() - delta),
                testfunc=lambda: w.winfo_y() > mh - wh
            ))
        elif side == W:
            w.place(x=-ww, y=0)
            delta = ww / self.units
            w.after(self.INTERVAL, lambda: self._cb_move(
                setfunc=lambda: w.place(x=w.winfo_x() + delta),
                testfunc=lambda: w.winfo_x() < 0
            ))
        else:
            raise ValueError('invalid side {}'.format(side))

    def slide_out(self):
        w = self.widget
        if self.playing.get():  # is playing?
            self.stop.set(True)  # set stop-var
            w.wait_variable(self.stop)  # wait until stop-var is set to False

        self.playing.set(True)  # set playing

        if callable(self.width): ww = self.width()
        elif self.width: ww = self.width
        else: ww = w.winfo_reqwidth()
        if callable(self.height): wh = self.height()
        elif self.height: wh = self.height
        else: wh = w.winfo_reqheight()

        mw = w.master.winfo_width()
        mh = w.master.winfo_height()
        side = self.side
        if side == N:
            delta = wh / self.units
            w.after(self.INTERVAL, lambda: self._cb_move(
                setfunc=lambda: w.place(y=w.winfo_y() - delta),
                testfunc=lambda: w.winfo_y() > -wh
            ))
        elif side == E:
            delta = ww / self.units
            w.after(self.INTERVAL, lambda: self._cb_move(
                setfunc=lambda: w.place(x=w.winfo_x() + delta),
                testfunc=lambda: w.winfo_x() < mw
            ))
        elif side == S:
            delta = wh / self.units
            w.after(self.INTERVAL, lambda: self._cb_move(
                setfunc=lambda: w.place(y=w.winfo_y() + delta),
                testfunc=lambda: w.winfo_y() < mh
            ))
        elif side == W:
            delta = ww / self.units
            w.after(self.INTERVAL, lambda: self._cb_move(
                setfunc=lambda: w.place(x=w.winfo_x() - delta),
                testfunc=lambda: w.winfo_x() > -ww
            ))
        else:
            raise ValueError('invalid side {}'.format(side))

    def _cb_move(self, setfunc, testfunc):
        if self.stop.get():  # if should stop
            print("Anim stopped")
            self.playing.set(False)  # stop playing
            self.stop.set(False)  # say it stopped
            return
        setfunc()
        if testfunc():
            self.widget.after(self.INTERVAL, lambda: self._cb_move(setfunc, testfunc))
        else:
            self.playing.set(False)
            print("Anim Done")


########################################################################################################################
# ZoomAnimation
########################################################################################################################


class ZoomAnimation:
    def __init__(self, widget: tk.Widget):
        self.w = widget

    def zoom_in(self):
        pass

    def zoom_out(self):
        pass


########################################################################################################################
# GifPlayer
########################################################################################################################


class GifPlayer:
    def __init__(self, widget: tk.Widget, fp: Union[str, io.FileIO], *, autoplay=True, size: Tuple[int, int] = None):
        self.widget = widget
        self.__is_playing = False
        image: Image.Image = Image.open(fp)
        if not image.is_animated:
            raise ValueError('image is not animated')

        self.frames = []
        self.frame = 0
        for frame in range(0, image.n_frames):
            image.seek(frame)
            img = image
            if size:
                img = image.resize(size)
            self.frames.append([
                image.info['duration'],
                ImageTk.PhotoImage(img)
            ])

        if autoplay:
            self.play()

    @property
    def is_playing(self):
        return self.__is_playing  # this method to made read-only

    def play(self):
        if self.__is_playing: return
        self.__is_playing = True
        self.__play_frame()

    def stop(self):
        self.__is_playing = False

    def __play_frame(self):
        if not self.__is_playing: return
        if self.frame >= len(self.frames):
            self.frame = 0
        duration, image = self.frames[self.frame]
        self.widget.configure(image=image)
        self.frame += 1
        self.widget.after(duration, self.__play_frame)
