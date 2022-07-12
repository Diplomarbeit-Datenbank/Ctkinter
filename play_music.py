"""

    Library to play Music on the PC or Pixel Boy

"""

from pygame import mixer

__date__ = '08.07.2021'
__completed__ = '10.08.2021'
__work_time__ = 'about 3 Hours'
__author__ = 'Christof Haidegger'
__version__ = '1.0'
__licence__ = 'Common Licence'
__debugging__ = 'Christof Haidegger'


mixer.init()


class thread_for_next_song_jump:
    """

        -> This class is to create a 'thread' which counts the seconds of the song, so the software knows, when the
           song clip is finnish

    """
    run = False

    def __init__(self, func, canvas) -> None:
        """

        :param func:   function which should be run, when the song is finnish
        :param canvas: canvas where the Media Player is on (this function needs tkinter.after() function of the canvas)
        """
        self.func = func
        self.canvas = canvas
        if self.func is not None:
            canvas.after(5, self.thread_for_next_song)
            type(self).run = True

    def thread_for_next_song(self) -> None:
        """

            -> This is the function, where the 'thread' is going to count the seconds of the running song

        """
        if int(mixer.music.get_pos()) != -1:
            pass
        else:
            type(self).run = False
            self.canvas.after(100, self.func)
            # print('fin thread normal')

        if type(self).run is True:
            self.canvas.after(100, self.thread_for_next_song)
        # else:
            # print('kill thread')

    def kill(self) -> None:
        """

            -> Kill the actually running thread

        """
        type(self).run = False
        # print('kill')


def play_music_file(file_path, func, canvas, thread=True) -> None:
    """

    :param thread:    if true it will be run the thread function
    :param file_path: path to the file which should be run (mp3 file)
    :param func:      function which should be run, when the mp3 file is finnish
    :param canvas:    canvas (no matter which) its just to use tkinter after function
    :return:          None if everything had been done correctly
    """
    if mixer.music.get_busy():
        mixer.music.stop()
    mixer.music.load(file_path)
    mixer.music.play()
    if thread:
        canvas.after(200, lambda: thread_for_next_song_jump(func, canvas))


def pause_music():
    """

        -> Pause the song clip, when it is not actually paused, else it resume it

    """
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        resume_music()


def resume_music():
    """

        -> resume the music clip

    """
    mixer.music.unpause()


def stop_music():
    """

        -> stop the music

    """
    mixer.music.stop()


def play_sound(file_path):
    if mixer.music.get_busy() == 0:
        sound = mixer.Sound(file_path)
        sound.play()

