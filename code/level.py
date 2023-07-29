import pygame

from debug import Debug
from config import WORLD_MAP, TILE_SIZE
from sprite import VisibleSprites, ObstacleSprites
from tile import Tile
from player import Player


class Level:
    def __init__(self, surface):
        self.display_surface = surface
        self.visible_sprites = VisibleSprites()
        self.obstacle_sprites = ObstacleSprites()
        self.player = None

        self._create_map()

    def render(self, dt):
        self.player.update(dt=dt)
        self.visible_sprites.draw(self.display_surface)

        self.visible_sprites.update()
        # Debug.d(self.obstacle_sprites)
        # print(self.player._direction)
        # Debug.d(self.player.__direction)

    def update(self):
        ...

    def _create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                match col:
                    case 'x':
                        Tile([self.visible_sprites, self.obstacle_sprites], pos=(x, y))
                    case 'p':
                        self.player = Player([self.visible_sprites], pos=(x, y))
                        self.visible_sprites.player_sprite = self.player
        if self.player is None: raise Exception('Missing player position in world map')
        else: self.player.set_obstacle_group(self.obstacle_sprites)
