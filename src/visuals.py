from tkinter import *
import math

class Catan_Visuals():

    def __init__(self, width, height):

        self.hex_radius = 5 * (width / height)
        self.hex_distance = 2 * self.hex_radius * math.cos(math.pi/6)    # The distance between the centers of two tiles

        self.window = Tk()
        self.window.title('Catan')

        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.pack()

        self.window.mainloop()

    # Draws a set of tiles for the board
    # hex_rad is the distance from the center of the hex to a point
    def draw_tiles(self, tiles):
        for t in tiles:
            self.draw_tiles(t, self.hex_radius, self.hex_distance)

    # takes in a tile's x,y,z co-ords and return xy graphical co-ords
    def get_tile_center(self, x, y, z):

        y_xcomp = y * math.cos(math.pi/6)
        y_ycomp = y * math.cos(math.pi/12)

        z_xcomp = z * math.cos(math.pi/6)
        z_ycomp = z * math.cos(math.pi/12)

        x_sum = x + y_xcomp - z_xcomp
        y_sum = y_ycomp + z_ycomp

        return x_sum * self.hex_distance, y_sum * self.hex_distance

    # Takes a tile central position, and radius of a hex
    def get_tile_points(self, center_pos, hex_rad):
        return []

    def draw_tile(self, tile, hex_rad, hex_distance):

        self.canvas.create_polygon()



app = Catan_Visuals(900, 900)

