import enum
import math
import random


class TileTypes(enum.Enum):
    sheep = 1
    wheat = 2
    wood = 3
    clay = 4
    ore = 5
    desert = 6


class PlayerColors(enum.Enum):
    red = 1
    blue = 2
    orange = 3
    white = 4


class Tile:

    # Uses Cube coordinates
    def __init__(self, x, y, z, tile_type):
        self.x = x
        self.y = y
        self.z = z
        self.type = tile_type

    # Determines if two tiles are next to one another
    def is_neighbor(self, tile):
        amnt = 0
        if self.x == tile.x:
            amnt += 1
        if self.y == tile.y:
            amnt += 1
        if self.z == tile.z:
            amnt += 1
        return amnt == 1

    def get_resource(self):
        return self.type


class Road:

    # The line between tiles
    def __init__(self, tile1, tile2, owner):
        if not tile1.is_neighbor(tile2):
            raise Exception("There was a road that was created two tiles that are not neighbors.")

        self.tile1 = tile1
        self.tile2 = tile2
        self.owner = owner


class Settlement:

    # A node between 3 tiles, could represent a settlement or city
    def __init__(self, tile1, tile2, tile3, owner):
        if not (tile1.is_neighbor(tile2) and tile1.is_neighbor(tile3) and tile2.is_neighbor(tile3)):
            raise Exception("There was a road that was created three tiles that are not neighbors.")

        self.tiles = (tile1, tile2, tile3)
        self.owner = owner
        self.is_city = False

    # Upgrades a settlement to a city
    def upgrade_to_city(self):
        self.is_city = True

    # Returns a list of the tile types that surround the settlement, if it is a city then the resources are doubled
    def get_resources(self):
        res = [t.get_resource() for t in self.tiles]
        if self.is_city:
            res = 2 * res
        return res


class Board:

    def __init__(self, radius, tile_type_collection):

        if radius > 0:
            self.tile_amnt = 1 + 6 * math.factorial(radius)
        else:
            raise Exception("The radius of the boards was less than one, the boards was unable to be constructed.")

        self.tiles = self.generate_tiles(radius, tile_type_collection)

    # Generates the tiles for the board
    def generate_tiles(self, radius, tile_type_collection):
        tiles = dict()

        # Fill the remain tiles, and shuffle them
        while len(tile_type_collection) < self.tile_amnt:
            tile_type_collection.append(TileTypes.desert)
        random.shuffle(tile_type_collection)

        # Make the tiles in the board
        for x in range(-radius, radius):
            for y in range(-radius, radius):
                for z in range(-radius, radius):
                    if x + y + z == 0:
                        tiles[(x, y, z)] = Tile(x, y, z, tile_type_collection.pop())
        return tiles
