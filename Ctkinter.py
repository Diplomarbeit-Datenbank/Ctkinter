"""
    Additional Package for tkinter

    This package support much more things thant tkinter (example: rounded corners, running gifs)
        -> How to use it:
            1. All function in this library are the same in use thant the tkinter functions
            2. The function only support a few more arguments like rounded_corners
            3. When calling for example tkinter.Button use Ctkinter.CButton to run this library
            4. This library requires a few modules which had to be installed before using
                -> 1. Pillow
                -> 2. numpy
                -> 3. opencv-python
                -> 4. termcolor
                -> 5. inspect
                -> 6. imageio


"""

from PIL import Image as _Image, ImageTk
from inspect import currentframe
from termcolor import colored
import tkinter as tk
import _tkinter
import numpy as np
import threading
import imageio
import time
import math
import cv2


__author__ = 'Christof Haidegger'
__date__ = '27.06.2021'
__completed__ = '16.07.2021'
__work_time__ = 'about 15 Hours'
__version__ = 'BETA VERSION 1.8 -> There may be some unknown issues left -> BETA VERSION 1.6 -> first stable version'
__licence__ = 'opensource(common licenced)'


def get_right_master(master):
    """

    :param master: master value in function
    :return: if master is a Ctkinter object or a tkinter object
    """
    try:
        return master['CObject']
    except _tkinter.TclError:
        return master


def get_line_number():
    """

    :return: the current line number
    """
    cf = currentframe()
    return cf.f_back.f_lineno


class Round_corners:
    """

        class for creating round corners on a tkinter canvas or a image
            -> it is normally not useful for the user -> this class is only used inside this file

    """

    def __init__(self):
        self.canvas = None
        self.image = None

    def rounded_corners_canvas(self, bg, width, height, c="round", outline=('', 0), max_rad=None, dash=None):
        """

        :param dash:    for striped lines for outline
        :param max_rad: max_radius for corners
        :param bg:      background of the polygon
        :param outline: the outline of the polygon
        :param width:   width of the button
        :param height:  height of the button
        :param c:       type of corner of the button
        :               -> create corners of the button
        """
        assert c == "round" or c == "rounded" or c == "angular" or None, "c must be round or rounded"
        step = height * 2
        if c == "rounded":
            c = int(height / 3)
        if c == "round":
            c = height - 1
            outline = ('', 1)  # unsupported operator for completely round button
        if c == "angular":
            c = 0
            step = 0
        if max_rad is not None:
            if c > max_rad:
                c = max_rad

        points = [2 + c, 2, 2 + c, 2, width - c, 2, width - c, 2, width, 2, width, 2 + c, width, 2 + c,
                  width, height - c, width, height - c, width, height, width - c, height, width - c, height,
                  2 + c, height, 2 + c, height, 2, height, 2, height - c, 2, height - c, 2, 2 + c, 2, 2 + c, 2, 2]

        return self.canvas.create_polygon(points, fill=bg, smooth=True, outline=outline[0], width=outline[1],
                                          splinesteps=step, dash=dash)

    def rounded_corners_image(self, width, height, c):
        """

        :param width:             length of the image (the image will be resized to that size)
        :param height:            width of the image (the image will be resized to that size)
        :param c:                 corner of the image, could be round or rounded
        :return:                    -> the new image with the rounded corners
        """
        assert c == "round" or c == "rounded" or c is None, "c must be round, rounded or angular"

        self.image = cv2.cvtColor(cv2.resize(self.image.copy(), (width, height)), cv2.COLOR_BGR2BGRA)

        ret_image = np.zeros((width, height, 4), dtype=np.uint8)

        diag = int(math.sqrt(width ** 2 + height ** 2))
        to_add = ((diag / 2 - width / 2) / 2)

        if c == "rounded":
            ret_image = cv2.circle(ret_image,
                                   (int(width / 2), int(height / 2)), int((diag / 2 + to_add)), (255, 255, 255, 255),
                                   int(to_add * 4))

        if c == "round":
            radius = (int(height / 2) + int((diag - (height / 2)) / 2) + int(to_add / 2) - 2) - 5
            ret_image = cv2.circle(ret_image, (int(width / 2), int(height / 2)),
                                   radius, (255, 255, 255, 255), int(diag - (height / 2)))

        ret_image = cv2.bitwise_not(ret_image)
        ret_image[np.where(ret_image == 255)] = self.image[np.where(ret_image == 255)]

        return ret_image

    def return_canvas(self):
        """

        :return: the rounded canvas
        """
        return self.canvas


class CButton:
    """

        This class is to create Buttons with round corners
            -> it is based on a tkinter Canvas but can used like a normal tkinter Button with the same parameters
            -> This Button support more additional function than tkinter Button
                1. master_color     -> this is required to create a background less tkinter canvas with round corners
                2. outline          -> this is to create a outline of the button
                3. change_color     -> this is the color which get the button filled, when it is on focus
                4. rounded_corners  -> this is to create round corners of the button (it looks really nice)
                5. image            -> to this parameter you only have to give the path to the image in not more
                6. pressing_color   -> this color rise up when the button is pressed

    """

    def __init__(self, master, bg='black', highlight_color='white', pressing_color='white', width=40, height=10,
                 text=None, font=('Sans', 12), fg='black', courser="hand2", outline=('', 1), rounded_corners='angular',
                 image=None, command=None, max_rad=None, dash=None):
        """

        :param master:          master (object, where the button should be placed)
        :param pressing_color:  color while button is pressed
        :param text:            text on the Button
        :param font:            font for the text on the Button
        :param fg:              color of the text on the Button
        :param courser:         example: hand1, hand2
        :param outline:         to draw the outline of the button (it is a color and the thick to set
                                -> tuple ex: ('black', 2)
        :param width:           width of the button
        :param height:          height of the button
        :param bg:              background of the button -> if None button will be transparent
                                NOTE: when you leve the mouse with the button the button will change to highlight_color
                                      if bg is None
                                      -> So use bg is None only if you place the Button on a other Button
        :param rounded_corners: create rounded corners ore not
        :param command:         set function as command for CButton

        -> minimal recommended variable sets:
            -> text, bg, master_color and command
        """

        right_master = get_right_master(master)

        self.CButton = tk.Canvas(right_master, width=width + 2, height=height + 2, bg=master['background'],
                                 highlightthickness=0, cursor=courser)

        self.change_to_highlight_color = False
        if bg is None:
            bg = master['background']
            self.change_to_highlight_color = True

        self.bg = bg
        self.command = command
        self.width = width
        self.height = height
        self.image = image
        self.color_conf_list = list()
        self.change_color = highlight_color
        self.pressing_color = pressing_color

        '# create rounded corners'
        polygon = Round_corners()
        polygon.canvas = self.CButton
        self.polygon = polygon.rounded_corners_canvas(self.bg, width, height, rounded_corners, outline, max_rad=max_rad,
                                                      dash=dash)
        self.CButton = polygon.return_canvas()

        if highlight_color is not None:
            self._change_color_command()
        if command is not None:
            self._set_command(command)
        if text is not None:
            self._set_text(text, font, fg)
        if image is not None:
            '# construction of the tuple: (file, round | rounded | angular, x | y position)'
            assert isinstance(image, tuple) is True, "image must be a tuple! example: ('image.png', 'round', (10, 10))"
            if len(image) == 3:
                self.image = (image[0], image[1], image[2], False)
                self._set_image(image[0], image[1], image[2], False)
            elif len(image) == 4:
                self._set_image(image[0], image[1], image[2], image[3])
            else:
                raise Exception('image param had to be at lead three parameters')

        self.params = {"background": bg, "CObject": self.CButton}

    def __getitem__(self, item):
        """

        :param item: item to get (normally background)
        :return: the item value
        """
        return self.params[item]

    def set_button_atributes(self, handler, item, set_command=True):
        """

           -> Configure the background color of the item to same color as the button when it is on highlight or pressed
           -> If set command is true the command also will be available when the handler is pressed

        :param handler:     normally the background canvas of a CtkButton
        :param item:        if handler is a Ctk Object: for Ctk.Button -> self.polygon, Ctk.Canvas -> self.outline
        :param set_command: if True, the command for the button will also set for this item on the Button
        :return:           configure the button like the background button
        """

        if self.command is not None and set_command is True:
            handler.bind("<Button-1>", lambda event: self._set_func())
            handler.bind("<ButtonRelease>", lambda event: self._fin_function(self.command))

        self.color_conf_list.append((handler, item))

    def config(self, **kwargs):
        """

        :param kwargs: kwargs for a normal tkinter button
        :return: configure the button with the kwargs arguments
        """
        if list(kwargs.keys())[0] == 'command':
            self._set_command(list(kwargs.values())[0])
        if list(kwargs.keys())[0] == 'image':
            self._set_image(*kwargs.get('image'), self.bg)

    def pack(self, *args, **kwargs):
        """

        : pack the button on the interface (attention fill function is not callable because of the fix size)
        """
        self.CButton.pack(*args, **kwargs)

    def place(self, x=None, y=None):
        """

        :param x: x position to place
        :param y: y position to place
        :           -> place the Button on the Interface
        """
        self.CButton.place(x=x, y=y)

    def destroy(self):
        """

        : destroy the CButton
        """
        self.CButton.destroy()

    def _change_color(self, leave):
        """

        :param leave: when ture: change the color, when false set transparency mode
        :                           -> change the color when moving the mouse over it
        """
        if not leave:
            self.CButton.itemconfig(self.polygon, fill=self.change_color)
            for handler, item in self.color_conf_list:
                handler.itemconfig(item, fill=self.change_color)
                handler.config(bg=self.change_color)

            # vlt fia die Katz bitte nachschauen
            if self.image is not None:
                self._set_image(self.image[0], self.image[1], self.image[2], self.image[3])
        else:
            if self.change_to_highlight_color is False:
                self.CButton.itemconfig(self.polygon, fill=self.bg)
            else:
                self.CButton.itemconfig(self.polygon, fill=self.change_color)
            for handler, item in self.color_conf_list:
                handler.itemconfig(item, fill=self.bg)
                handler.config(bg=self.bg)

            # vlt fia die Katz bitte nachschauen
            if self.image is not None:
                self._set_image(self.image[0], self.image[1], self.image[2], self.image[3])

    def _change_color_command(self):
        """

        : change the color
        """
        self.CButton.bind('<Enter>', lambda a: self._change_color(False))
        self.CButton.bind('<Leave>', lambda a: self._change_color(True))

    def _set_func(self):
        self.CButton.itemconfig(self.polygon, fill=self.pressing_color)
        for handler, item in self.color_conf_list:
            handler.itemconfig(item, fill=self.pressing_color)
            handler.config(bg=self.pressing_color)

        # vlt fia die Katz bitte nachschauen
        if self.image is not None:
            self._set_image(self.image[0], self.image[1], self.image[2], self.image[3])

    def _fin_function(self, func):
        """
        :param func: the function which is to start, when the button is pressed
                :               -> run the function

        : when function is finished, go back to self.bg color
        """
        self.CButton.itemconfig(self.polygon, fill=self.change_color)
        for handler, item in self.color_conf_list:
            handler.itemconfig(item, fill=self.change_color)
            handler.config(bg=self.change_color)

        # vlt fia die Katz bitte nachschauen
        if self.image is not None:
            self._set_image(self.image[0], self.image[1], self.image[2], self.image[3])

        func()

    def _set_command(self, func):
        """

        :param func: the function which is to run
        :               -> run the function
        """
        self.CButton.bind("<Button-1>", lambda event: self._set_func())
        self.CButton.bind("<ButtonRelease>", lambda event: self._fin_function(func))

    def _set_text(self, text, font, fg):
        """

        :param text: text to set
        :param font: font of the text
        :param fg:   color of the text
        :               -> change text and the color
        """
        self.CButton.create_text(int(self.width / 2), int(self.height / 2) + 1, fill=fg, font=font,
                                 text=text)

    def get_canvas(self):
        return self.CButton

    def _set_image(self, image_path, c, pos, full):
        """

        :param image_path: path to the image, which is to set
        :param c:          corners (could be round, rounded or angular)
        :param pos:        position of the image on the button
        """
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if c != "angular":
            round_corn = Round_corners()
            round_corn.image = image
            if full is False:
                new_image = round_corn.rounded_corners_image(int(self.width / 3), int(self.height) - 10, c)
            else:
                new_image = round_corn.rounded_corners_image(full[0], full[1], c)

        else:
            if full is False:
                new_image = cv2.resize(image.copy(), (int(self.width / 3), int(self.height) - 10))

            else:
                new_image = cv2.resize(image.copy(), (full[0], full[1]))

        rgba_image = cv2.cvtColor(new_image.copy(), cv2.COLOR_BGRA2RGBA)
        pil_array = _Image.fromarray(rgba_image)
        self.tk_image = ImageTk.PhotoImage(image=pil_array)
        self.CButton.create_image(pos[0], pos[1], image=self.tk_image)


class CCanvas:
    """
        This function is able to create a round, rounded or angular tkinter Canvas

        -> This Canvas has the same functions as the Canvas from the tkinter Library and a few more
                New functions:
                    1. create_gif(gif_path, corner, size, pos):
                        -> run a gif on the tkinter, when the Canvas is in focus
                    2. create_image(corner, bg, width, height, pos, image_path, read_from_path=True):
                        -> in this function you only need to put the path of the image in, no ImageTk is required
                        -> you also able to round, rounded or angular the image
                    3. get_canvas():
                        -> it return the tkinter Canvas itself

    """
    # to count the warnings
    warning_counter = 0

    def __init__(self, master, bg='gray', size=(300, 300), corners='rounded', max_rad=None, outline=('', 0), dash=None):
        """

        :param master:         item, where the Canvas should be placed
        :param bg:             background of the Canvas
        :param size:           size of the Canvas (size[0] = width, size[1] = height)
        :param corners:        could be round, rounded or angular
        :param outline:        when outline should be drawn (example: outline=('black', 1))
        """

        self._tk_image = None
        self._tk_image_list, self._canvas_image_list = list(), list()
        self.image_counter = 0
        self.gif = None
        self.focus = False
        self.bg = bg
        self.corners = corners
        self.size = size
        self.outline_color = outline
        self.max_rad = max_rad

        right_master = get_right_master(master)

        round_corn = Round_corners()
        round_corn.canvas = tk.Canvas(right_master, bg=master['background'], width=size[0] + 2, height=size[1] + 2,
                                      highlightthickness=0)
        self.outline = round_corn.rounded_corners_canvas(bg, size[0], size[1], corners, outline, max_rad=max_rad,
                                                         dash=dash)
        self.Canvas = round_corn.return_canvas()

        self.params = {"background": bg, "CObject": self.Canvas}

    def get_all_items(self):
        print(self.Canvas.find_all())

    def __getitem__(self, item):
        """

        :param item: item to get (normally background)
        :return: the item value
        """
        return self.params[item]

    def after(self, *args, **kwargs):
        self.Canvas.after(*args, **kwargs)

    def config(self, **kwargs):
        """
            THIS FUNCTION IS NOT GREAT AT ALL! It does not work well because by changing the background the other items
            will be behind the background
        :param kwargs:
        :return:
        """
        if list(kwargs.keys())[0] == 'size':
            print(colored('[Ctkinter: Warning: ' + str(type(self).warning_counter) + ' in Line: ' +
                          str(get_line_number()) + ']' ' by changing the size, the '
                                                   'background color must be renewed', 'yellow'))
            type(self).warning_counter += 1
            self.size = (kwargs.get('size')[0], kwargs.get('size')[1])
            self.Canvas.config(width=int(kwargs.get('size')[0]), height=int(kwargs.get('size')[1]))
            self.Canvas.delete(self.outline)
            self._change_background(self.bg)

        if list(kwargs.keys())[0] == 'bg':
            self._change_background(kwargs.get('bg'))

    def _change_background(self, new_bg):
        """

        :param new_bg: new background
        :return: change the background of the canvas
        """
        print(colored('[Ctkinter: Warning: ' + str(type(self).warning_counter) + ' in Line: ' +
                      str(get_line_number()) + '] All objects on canvas are deleted with changing the background',
                      'yellow'))

        type(self).warning_counter += 1
        round_corn = Round_corners()
        self.Canvas.delete('all')
        round_corn.canvas = self.Canvas
        self.outline = round_corn.rounded_corners_canvas(new_bg, self.size[0], self.size[1],
                                                         self.corners, self.outline_color, max_rad=self.max_rad)
        self.Canvas = round_corn.return_canvas()
        self.params = {"background": new_bg, "CObject": self.Canvas}

    def update(self):
        """

        :update the tkinter Canvas
        """
        self.Canvas.update()

    def winfo_id(self):
        """

        :return: -> id of the window (id of the Canvas)
        """
        return self.Canvas.winfo_id()

    def place(self, x, y):
        """

        :param x: x position
        :param y: y position
        :           -> place the canvas on the given x and y position
        """
        self.Canvas.place(x=x, y=y)

    def pack(self, *args, **kwargs):
        """

        :param args:   args from tkinter library
        :param kwargs: kwargs from tkinter library
        :                -> pack the Canvas on the master
        """
        self.Canvas.pack(*args, **kwargs)

    def create_image(self, corner, width, height, pos, image_path, transparent=False, read_from_path=True):
        """

        :param transparent:
        :param read_from_path: when Ture: the image will be read, when False the image had already been read
                                                                  -> set image_path = cv2.imread('image_path')
        :param image_path: when read_from_path     -> path of the image on storage,
                           when not read_from_path -> imread from cv2 (example: cv2.imread('image_path'))

        :param corner: could be round, rounded or angular
        :param width:  with of the image
        :param height: height of the image
        :param pos:    position of the image on the Canvas
        :                   -> draw the image on the Canvas
        """

        if read_from_path is True:
            if transparent is False:
                image = cv2.imread(image_path)
            else:
                image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        else:
            if transparent is False:
                image = cv2.cvtColor(image_path, cv2.COLOR_RGB2BGR)
            else:
                image = cv2.cvtColor(image_path, cv2.COLOR_RGB2BGRA)

        """
        if transparent is True and corner != 'angular':
            raise Exception('gif animation or images with transparent background could not be rounded or round -> '
                            'use angular')
        """

        if corner != "angular":
            round_corn = Round_corners()
            round_corn.image = image

            new_image = round_corn.rounded_corners_image(width, height, corner)
        else:
            new_image = cv2.resize(image.copy(), (width, height))

        rgb_image = cv2.cvtColor(new_image.copy(), cv2.COLOR_BGR2RGBA)
        pil_array = _Image.fromarray(rgb_image)
        self._tk_image = ImageTk.PhotoImage(image=pil_array)
        self._tk_image_list.append(self._tk_image)
        canvas_image = self.Canvas.create_image((pos[0], pos[1]),
                                                image=self._tk_image_list[len(self._tk_image_list) - 1])
        self._canvas_image_list.append(canvas_image)
        self.Canvas.image = self._tk_image_list[len(self._tk_image_list) - 1]

    def clear_image_list(self):
        """

        :  -> clear the image list, to get no memory error
        """
        self._tk_image_list = list()

    def _run_animation(self, gif_len, transparent, corner, size, pos, large=False):
        """

        :param corner: could be round, rounded or angular
        :param size:   size of the image
        :param pos:    position of the image
        :                 -> run the animation
        """
        frame = self.gif.get_data(self.image_counter)
        ret = True
        if ret is True:
            if self.image_counter != 0:
                if len(self._canvas_image_list) > 1:
                    try:
                        self.Canvas.delete(self._canvas_image_list[len(self._canvas_image_list) - 2])
                    except _tkinter.TclError:
                        print(colored('[Ctkinter: Error: ' + str(type(self).warning_counter) + ' in Line: ' +
                                      str(get_line_number()) + '] image to destroy wos not found raise execution',
                                      'red'))

                        type(self).warning_counter += 1

            frame = cv2.resize(frame, size)
            self.create_image(corner, size[0], size[1], pos, frame, transparent=transparent,
                              read_from_path=False)
            self.image_counter += 1
            if self.image_counter == gif_len:
                self.image_counter = 0
                self.clear_image_list()

            if large is True:
                self.clear_image_list()

    def _start_animation(self, gif_len, transparent, corner, size, pos, large, speed):
        """

        :param corner: could be round, rounded or angular
        :param size:   size of the image
        :param pos:    position of the image
        :                  -> start run the animation
        """
        while self.focus is True:
            try:
                self._run_animation(gif_len, transparent, corner, size, pos, large)
            except _tkinter.TclError:
                print(colored('[Ctkinter: Error: ' + str(type(self).warning_counter) + ' in Line: ' +
                              str(get_line_number()) +
                              '] Gif image could not be created -> destroy the actually gif', 'red'))
                type(self).warning_counter += 1
                break
            if speed == 'fast':
                time.sleep(0.04)
            if speed == 'normal':
                time.sleep(0.06)
            if speed == 'slow':
                time.sleep(0.08)

    def _focus_false(self):
        """

        : canvas not on focus
        """
        self.focus = False

    def _focus_true(self, gif_len, transparent, corner, size, pos, large, speed):
        """

        :param corner: could be round, rounded or angular
        :param size:   size of the image
        :param pos:    position of the image
        :                   -> canvas in focus -> run the gif animation
        """
        self.focus = True
        threading.Thread(target=self._start_animation, args=(gif_len, transparent, corner, size, pos, large, speed
                                                             )).start()

    def create_gif(self, gif_path, corner, size, pos, transparent=False, set_half_gif_time=False, speed='normal'):
        """

        :param speed: 
        :param transparent:
        :param set_half_gif_time: set the gif time to half
        :param gif_path: path of the gif in storage
        :param corner:   could be round, rounded or angular
        :param size:     size of the gif
        :param pos:      position of the gif
        :                   -> set a gif image on the canvas
        """
        try:
            self.gif = imageio.get_reader(gif_path)
        except FileNotFoundError:
            raise FileNotFoundError('Gif does not exist')
        gif_data = cv2.VideoCapture(gif_path)
        gif_len = gif_data.get(7)
        large = False
        if self.gif.get_length() > 300:
            large = True

        if set_half_gif_time is True:
            self.image_counter = int(self.gif.get_length() / 2)

        self._run_animation(gif_len, transparent, corner, size, pos, large)
        self.Canvas.bind('<Enter>', lambda event: self._focus_true(gif_len, transparent, corner, size, pos, large,
                                                                   speed))
        self.Canvas.bind('<Leave>', lambda event: self._focus_false())

    def create_text(self, *args, **kwargs):
        """

        :param args:   args from tkinter library
        :param kwargs: kwargs from tkinter library
        :                   -> create text on canvas
        """
        self.Canvas.create_text(*args, **kwargs)

    def create_line(self, *args, **kwargs):
        """

        :param args:   args from tkinter library
        :param kwargs: kwargs from tkinter library
        :                 -> create line on canvas
        """
        return self.Canvas.create_line(*args, **kwargs)

    def bind(self, *args, **kwargs):
        """

        :param args:   args from tkinter library
        :param kwargs: kwargs from tkinter library
        :                   -> bind function on canvas
        """
        return self.Canvas.bind(*args, **kwargs)

    def create_oval(self, *args, **kwargs):
        """

        :param args:   args from tkinter library
        :param kwargs: kwargs from tkinter library
        :                   -> create oval on canvas
        """
        return self.Canvas.create_oval(*args, **kwargs)

    def create_rectangle(self, *args, **kwargs):
        """

        :param args:   args from tkinter library
        :param kwargs: kwargs from tkinter library
        :                   -> create rectangle on canvas
        """
        return self.Canvas.create_rectangle(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """

        :param args:    args from tkinter library
        :param kwargs:  kwargs from tkinter library
        :                    -> delete item on canvas
        """
        return self.Canvas.delete(*args, **kwargs)

    def itemconfig(self, *args, **kwargs):
        """

        :param args:   args from tkinter library
        :param kwargs: kwargs from tkinter library
        :                   -> configure item on canvas
        """
        return self.Canvas.itemconfig(*args, **kwargs)

    def get_canvas(self):
        """

        :return: -> the Canvas itself
        """
        return self.Canvas

    def destroy(self):
        """

        -> destroy the Canvas
        """
        self.Canvas.destroy()

    def change_outline(self, new_outline):
        self.itemconfig(self.outline, outline=new_outline)


class CLabel:
    """
        This function is to create a Label with rounded corners
        All functions of tkinter label are given and a few more:
            1. max_rad:   -> it is the max radius of the corner from the Button
            2. corner:    -> to create rounded corners of the label three functions are available
            3. outline:   -> this is to draw the outline of the label
    """

    def __init__(self, master, bg='white', size=(100, 20), text=None, fg='black', font=('Sans', 12),
                 corner='rounded', max_rad=None, outline=('', 0), anchor='NW', variable_text=False,
                 enter_hit=(False, None), text_place=(10, 10)):
        """

        :param master:         master, where the Label should be placed
        :param bg:             background of the label
        :param size:           size of the label (size[0] = width, size[1] = height)
        :param text:           text on the label
        :param fg:             color of the text
        :param font:           font of the text
        :param corner:         could be round, rounded or angular
        :param max_rad:        max rad of the rounded label
        :param outline:        when outline should be drawn try: ('black', 2)
        """

        self.text = text
        self.font = font
        self.variable_text_widget = None
        change_size = False

        if size[0] is None:
            change_size = True
            size = (75, size[1])

        self.CLabel = CCanvas(master, bg, size, corner, max_rad=max_rad, outline=outline)

        if change_size is True:
            size = (int(self.get_text_len_in_px() + 10), size[1])
            self.CLabel.config(size=size)

        if text is not None:
            if variable_text is False:
                if anchor == 'NW':
                    self.CLabel.create_text(text_place[0], text_place[1], text=text, anchor=tk.NW, font=font, fill=fg)

                else:
                    self.CLabel.create_text(int(size[0] / 2), int(size[1] / 2), text=text, anchor=tk.CENTER, font=font,
                                            fill=fg)
            else:
                self._create_variable_text(fg, size, bg, text, enter_hit)

    def _create_variable_text(self, fg, size, bg, text, set_enter_hit=(False, None)):
        """

        :param size:          size of the variable text
        :param bg:            background of the variable text
        :param text:          text in the variable text widget
        :param set_enter_hit: if a event raises when enter (return) is hit
        :return:              create the changeable text widget on the label
        """

        self.variable_text_widget = tk.Entry(self.CLabel.get_canvas(), width=int((size[0] / 10) - 14), font=self.font,
                                             bg=bg, insertbackground='black', bd=0, fg=fg)

        self.variable_text_widget.insert(tk.END, text)
        self.variable_text_widget.place(x=10, y=12)

        if set_enter_hit[0] is not False:
            self.variable_text_widget.bind('<Return>',
                                           lambda a: self._run_enter_hit_function(set_enter_hit[1],
                                                                                  self.variable_text_widget))

    def _run_enter_hit_function(self, func, variable_text):
        """

        :param func:          run the function when enter is hit
        :param variable_text: the variable text widget itself
        :return:              run the function
        """
        self.CLabel.get_canvas().focus_set()
        func(variable_text)

    def get_canvas(self):
        """

        :return: the tkinter Canvas of the CLabel
        """
        return self.CLabel.get_canvas()

    def config(self, **kwargs):
        """

        :param kwargs: bg is the only available until now
        :return:
        """
        if list(kwargs.keys())[0] == 'bg':
            self.CLabel.config(bg=kwargs.get('bg'))
            if self.variable_text_widget is not None:
                self.variable_text_widget.config(bg=kwargs.get('bg'))

    def get_text_len_in_px(self):
        """
            Attention! This function is not really great but it works!

        :return: the len of the text in px
        """
        test_label = tk.Label(None, text=self.text, font=self.font)
        test_label.place(x=100000, y=100000)  # this is not nice but it works
        self.CLabel.update()
        text_len = test_label.winfo_width()
        test_label.destroy()

        return text_len

    def place(self, x, y):
        """

        :param x: x coordinate to place
        :param y: y coordinate to place
        :             -> the CLabel will be placed on the given x and y coordinates
        """
        self.CLabel.place(x=x, y=y)

    def pack(self, *args, **kwargs):
        """

        :param args:   args of the pack function from tkinter
        :param kwargs: kwargs of the pack function from tkinter
        :                   -> the CLabel will be packed
        """
        self.CLabel.pack(*args, **kwargs)

    def destroy(self):
        """

        :return: destroy the CLabel and the background tkinter Canvas
        """
        self.CLabel.destroy()


class TextAnimation:
    """

        -> Function is only BETA!!! You are not able to run the text faster, or slower, there is just one single speed
           This is because of the Windows Scheduler!
                                 -> When sleep function is run -> Windows run other threads before continue the
                                                                  _run_animation thread
                                 -> That means -> When sleep before moving the label x-1 Windows run a other thread
                                               -> The time, to finnish that thread take a small time longer than the
                                                  sleep time. -> Means there is only one time to sleep where only one
                                                                 thread is started -> This time is tested: 0.005s
                                                                                   -> This is may not the best time
                                                                                      so keep this in one eye

    """

    def __init__(self, master, bg, size, text, font, fg, label_place=(10, 5), text_space='default', 
                 test_delay=0):
        """

        :param master:      master for the animated text widget
        :param bg:          background for the animated label
        :param size:        size for the animated label
        :param text:        text on the animated label
        :param font:        font for the text
        :param fg:          color of the text
        :param label_place: place for the label on the animated text label -> that had nothing do do with the place on
                            the given master!
        """
        self.label_place_y = label_place[1]
        space = int(size[0] / 5.6)
        if text_space == 'default':
            self.text = text + int(size[0] / 5.6) * ' ' + text
        else:
            self.text = text + text_space * ' ' + text
            space = text_space

        self.size = size
        self.run = False
        self.text_pos_x = 0

        self.animated_text = tk.Frame(master=master, bg=bg, width=size[0], height=size[1])
        self._text_label = tk.Label(self.animated_text, text=self.text, bg=bg, font=font, fg=fg)

        self._text_label.place(x=label_place[0], y=label_place[1])
        self._text_label.update()
        text_width = self._text_label.winfo_width()
        self.animation_len_in_px = ((text_width - text_space) / 2) + test_delay
        self.animated_text.bind('<Enter>', lambda event: self._start_animation(text_width))

    def _stop_animation(self, text_width):
        """
            -> Stop the animated text widget and set the text to start value (0px)

        """
        self.run = False
        self.text_pos_x = 10
        self._change_x_position(text_width)
        self.animated_text.bind('<Enter>', lambda event: self._start_animation(text_width))

    def _run_text_animation(self, text_width):
        """

        :param text_width: width of the text widget
        """
        self._change_x_position(text_width)
        if -1 * self.text_pos_x >= self.animation_len_in_px:
            self._stop_animation(text_width)

        if self.run is True:
            self.animated_text.after(10, lambda: self._run_text_animation(text_width=text_width))

    def _start_animation(self, text_width):
        """

        :param text_width: width of the text widget
        """
        self.run = True
        self.animated_text.unbind('<Enter>')
        self.animated_text.after(10, lambda: self._run_text_animation(text_width=text_width))

    def _change_x_position(self, text_width):
        """

        :param text_width: width of the text widget
        """
        self._text_label.place_configure(x=self.text_pos_x, y=self.label_place_y)
        if self.text_pos_x >= (text_width * -1):
            self.text_pos_x -= 1
        else:
            self.text_pos_x = self.size[0]


def main():
    """

        -> Test the Text Animation Class
    """
    root = tk.Tk()
    root.title('Test Animated Text')
    root.geometry('450x200')

    text = TextAnimation(root, 'gray', (400, 40), text='Masked Wolf Astronaut in the ocean lyrics', 
                         font=('Helvetica', 15),
                         fg='white', label_place=(10, 7), text_space=40, test_delay=130)
    text.animated_text.place(x=20, y=20)

    root.mainloop()


if __name__ == '__main__':
    main()
