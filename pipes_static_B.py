"""Author: Benjamnin Dicken, 2019

   Written for CS 110, borrowed for CS 120"""



import tkinter
import time

import sys



class graphics:
    def __init__(self, w, h, title):
        ''' Initialize the graphics object.
        Creates a new tkinter Tk object,
        and a tkinter Canvas object,
        placed insize the Tk object.
        '''
        self.primary = tkinter.Tk()
        self.primary.title(title)
        self.primary.geometry('%dx%d+%d+%d' % (w, h, 50, 100))
        self.canvas = tkinter.Canvas(self.primary, width=w, height=h, highlightthickness=0)
        self.canvas.focus_set()
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.__handle_motion()

        self._priv_data = None

        self.setup_kill_events()

    def setup_kill_events(self):
        self.is_killed = False

        def kill_wind(e):
            self.primary.destroy()
            self.is_killed = True
        def kill_prog(e):
            sys.exit(1)

        self.canvas.bind("<Escape>",    kill_wind)
        self.canvas.bind("<Control-c>", kill_prog)

        # sometimes, if you don't do this, then the window shows up but doesn't
        # have focus - but that is *really* annoying, because then the keyboard
        # commands don't work.
        self.canvas.focus_force()

        # not sure why this is necessary.  But if I don't do this, then the key
        # presses don't get noticed.
        self.primary.update()

    def is_destroyed(self):
        try:
            return self.primary.winfo_exists() != 1
        except:
            return True


    def mainloop(self):
        self.primary.mainloop()



    # BEGIN PRIVATE FUNCTION(S)

    def __handle_motion(self):
        ''' Ensure mouse x and y coordinates are updated when mouse moves.
        '''
        def motion_action(event):
            self.mouse_x = event.x
            self.mouse_y = event.y
        self.canvas.bind('<Motion>', motion_action)

    # END PRIVATE FUNCTION(S)



    def resize(self, width, height):
        self.primary.geometry(str(width) + 'x' + str(height))

    def text(self, x, y, content, fill='black', size=17):
        ''' Draw text on the canvas.
        Must always specify the text, x, y position.
        Can optionally specify the fill color and size.
        '''
        text = self.canvas.create_text(x, y, text=content, fill=fill, font=('Arial', size), anchor='nw')
        self.canvas.move(text, 0, 0)

    def set_left_click_action(self, callee):
        ''' Call the callee function whenever the left click happens.
        callee should take two parameters, the mouse x and mouse y coordinates.
        '''
        def left_click_action(event):
            callee(self, event.x, event.y)
        ''' <Button-1> is the left-most mouse button '''
        self.canvas.bind('<Button-1>', left_click_action)

    def set_right_click_action(self, callee):
        ''' Call the callee function whenever the right click happens.
        callee should take two parameters, the mouse x and mouse y coordinates.
        '''
        def right_click_action(event):
            callee(self, event.x, event.y)
        ''' <Button-2> or <Button-3> is the right-most mouse button.
        Both are set just in case '''
        self.canvas.bind('<Button-2>', right_click_action)
        self.canvas.bind('<Button-3>', right_click_action)

    def set_keyboard_action(self, callee):
        ''' Call the callee function whenever a keyboard key is pressed. callee
            should take one parameter, a str representing the key.  For simple
            characters (alphanumerics and probably others), this works the same
            as Ben's version (which sent event.char instead of event.keysym).
            However, it is more general; every single key on the keyboard has a
            user-visible string that encodes it: "Shift_R", "F11", "KP_0", etc.
        '''
        self.canvas.bind('<KeyPress>', lambda event: callee(self, event.keysym))

    def get_color_string(self, red, green, blue):
        ''' accepts three ints that should represent and RGB color.
        Returns a hex string'''
        hex_string = hex(red)[2:].rjust(2, '0') + \
                     hex(green)[2:].rjust(2, '0') + \
                     hex(blue)[2:].rjust(2, '0')
        return '#' + hex_string

    def triangle(self, x1, y1, x2, y2, x3, y3, fill='black'):
        ''' Draw a triangle.
        The three corners of the triangle are specified with the parameter coordinates.
        '''
        r = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=fill)
        self.canvas.move(r, 0, 0)

    def line(self, x1, y1, x2, y2, fill='black', width=3):
        ''' Draw a line.
        The two ends of the line are specified with the parameter coordinates.
        '''
        r = self.canvas.create_line(x1, y1, x2, y2, fill=fill, width=width)
        self.canvas.move(r, 0, 0)

    def ellipse(self, x, y, w, h, fill='black'):
        ''' Draw an ellipse on the canvas.
        Specify x, y (center of ellipse) and width / height.
        '''
        r = self.canvas.create_oval(x-(w/2), y-(h/2), x+(w/2), y+(h/2), fill=fill)
        self.canvas.move(r, 0, 0)

    def rectangle(self, x, y, w, h, fill='black'):
        ''' Draw a rectangle on the canvas.
        Specify x, y (top-left corner) and width / height.
        '''
        r = self.canvas.create_rectangle(x, y, x+w, h+y, fill=fill, outline='')
        self.canvas.move(r, 0, 0)

    def update(self):
        ''' Does an idle task update and regular update.
        '''
        self.primary.update_idletasks()
        self.primary.update()

    def frame_space(self, frame_rate):
        ''' Sleeps for a time that corresponds to the provided frame rate.
        '''
        sleep_ms = 1.0 / float(frame_rate)
        time.sleep(sleep_ms)

    def update_frame(self, frame_rate):
        ''' Updates and sleeps.
        This should be called at the end of each iteration of a users draw loop.
        '''
        self.update()
        self.frame_space(frame_rate)

    def clear(self):
        ''' Clears the canvas.
        '''
        self.canvas.delete('all')



    # BEGIN PRIVATE DATA HANDLING

    def set_private_data(self, data):
        assert data is not None
        self._priv_data = data

    def get_private_data(self):
        assert self._priv_data is not None
        return self._priv_data

    # END PRIVATE DATA HANDLING


import random

def create_grey_back(win, x, y): 
    win.rectangle(x, y, 85, 85, "grey")

def black_mid_square(win, x, y):
    x += 27.5
    y += 27.5
    win.rectangle(x, y, 30, 30, "black")

def blue_mid_square(win, x, y): 
    x += 32.5
    y += 32.5
    win.rectangle(x, y, 20, 20, "blue")

def half_down(win, x, y):
    x += 40
    y += 40
    win.rectangle(x, y, 5, 45, "black")

def blue_half_down(win, x, y):
    x += 41.5
    y += 40
    win.rectangle(x, y, 1.5, 45, "blue")

def half_up(win, x, y):
    x += 40
    win.rectangle(x, y, 5, 45, "black")

def blue_half_up(win, x, y):
    x += 41.5
    win.rectangle(x, y, 1.5, 45, "blue")

def half_left(win, x, y):
    y += 40
    win.rectangle(x, y, 45, 5, "black")

def blue_half_left(win, x, y):
    y += 41.5
    win.rectangle(x, y, 45, 1.5, "blue")

def half_right(win, x, y):
    y += 40
    x += 40
    win.rectangle(x, y, 45, 5, "black")

def blue_half_right(win, x, y):
    y += 41.5
    x += 40
    win.rectangle(x, y, 45, 1.5, "blue")

def horizontal(win, x, y): 
    y += 40
    win.rectangle(x, y, 85, 5, "black")

def blue_horizontal(win, x, y): 
    y += 41.5
    win.rectangle(x, y, 85, 1.5, "blue")

def verticle(win, x, y): 
    x += 40
    win.rectangle(x, y, 5, 85, "black")

def blue_verticle(win, x, y): 
    x += 41.5
    win.rectangle(x, y, 1.5, 85, "blue")

def tile_r1_c1(win, x, y):
    create_grey_back(win, x, y)
    half_down(win, x, y)
    half_right(win, x, y)

def tile_r1_c2(win, x, y):
    create_grey_back(win, x, y)
    horizontal(win, x, y)

def tile_r1_c3(win, x, y): 
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_right(win, x, y)

def tile_r1_c4(win, x, y):
    create_grey_back(win, x, y)
    half_down(win, x, y)
    half_left(win, x, y)

def tile_r1_c5(win, x, y):
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_down(win, x, y)

def tile_r2_c1(win, x, y):
    create_grey_back(win, x, y)
    verticle(win, x, y)

def tile_r2_c2(win, x, y):
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_down(win, x, y)
    blue_mid_square(win, x, y)
    blue_half_down(win, x, y)

def tile_r2_c3(win, x, y):
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_left(win, x, y)

def tile_r2_c4(win, x, y):
    create_grey_back(win, x, y)
    half_up(win, x, y)
    horizontal(win, x, y)

def tile_r2_c5(win, x, y): 
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_right(win, x, y)

def tile_r3_c1(win, x, y):
    create_grey_back(win, x, y)
    horizontal(win, x, y)
    half_down(win, x, y)

def tile_r3_c2(win, x, y):
    create_grey_back(win, x, y)
    verticle(win, x, y)
    half_right(win, x, y)
    blue_half_right(win, x, y)
    blue_verticle(win, x, y)

def tile_r3_c3(win, x, y):
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    verticle(win, x, y)
    half_left(win, x, y)
    blue_mid_square(win, x, y)
    blue_verticle(win, x, y)
    blue_half_left(win, x, y)

def tile_r3_c4(win, x, y):
    create_grey_back(win, x, y)
    horizontal(win, x, y)
    half_down(win, x, y)

def tile_r3_c5(win, x, y): 
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_left(win, x, y)

def tile_r4_c1(win, x, y):
    create_grey_back(win, x, y)
    half_down(win, x, y)
    half_right(win, x, y)
    blue_half_down(win, x, y)
    blue_half_right(win, x, y)

def tile_r4_c2(win, x, y):
    create_grey_back(win, x, y)
    horizontal(win, x, y)
    half_up(win, x, y)
    blue_horizontal(win, x, y)
    blue_half_up(win, x, y)
    
def tile_r4_c3(win, x, y):
    create_grey_back(win, x, y)
    half_up(win, x, y)
    half_right(win, x, y)
    blue_half_up(win, x, y)
    blue_half_right(win, x, y)

def tile_r4_c4(win, x, y):
    create_grey_back(win, x, y)
    verticle(win, x, y)
    half_right(win, x, y)

def tile_r4_c5(win, x, y): 
    create_grey_back(win, x, y)
    horizontal(win, x, y)
    half_up(win, x, y)

def tile_r5_c1(win, x, y):
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_down(win, x, y)

def tile_r5_c2(win, x, y):
    create_grey_back(win, x, y)
    half_left(win, x, y)
    half_up(win, x, y)

def tile_r5_c3(win, x, y):
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_right(win, x, y)

def tile_r5_c4(win, x, y):
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_down(win, x, y)

def tile_r5_c5(win, x, y): 
    create_grey_back(win, x, y)
    black_mid_square(win, x, y)
    half_down(win, x, y)

def draw_all_tiles(win):
    tile_functions = [
        tile_r1_c1, tile_r1_c2, tile_r1_c3, tile_r1_c4, tile_r1_c5,
        tile_r2_c1, tile_r2_c2, tile_r2_c3, tile_r2_c4, tile_r2_c5,
        tile_r3_c1, tile_r3_c2, tile_r3_c3, tile_r3_c4, tile_r3_c5,
        tile_r4_c1, tile_r4_c2, tile_r4_c3, tile_r4_c4, tile_r4_c5,
        tile_r5_c1, tile_r5_c2, tile_r5_c3, tile_r5_c4, tile_r5_c5
    ]
    
    for row in range(5):
        for col in range(5):
            x = 10 + col * 98
            y = 10 + row * 98
            random_index = random.randint(0, len(tile_functions) - 1)
            tile_function = tile_functions[random_index]
            tile_function(win, x, y)

def main():
    win = graphics(500, 500, "Pipes Static B")
    draw_all_tiles(win)
    win.mainloop()

main()
