import pygame
from config import *
from sprite import Sprite


class Tile(Sprite):
    def __init__(self, groups, pos, res_dir = './graphics/test/rock.png'):
        super().__init__(groups, pos, res_dir)
