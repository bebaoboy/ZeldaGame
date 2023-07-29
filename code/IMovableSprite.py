import pygame

from debug import Debug
from sprite import Sprite

DIR_HORIZONTAL = 'horizontal'
DIR_VERTICAL = 'vertical'


class IMovableSprite(Sprite):
    def __init__(self, groups, pos, res_dir):
        super().__init__(groups, pos, res_dir)
        self._direction = pygame.Vector2(0, 0)
        self._target = self._prev_target = pos
        self._pos = pos
        self.speed = 3
        self.min_speed = 2
        self.max_speed = 3
        self.delta_speed = 0.01
        self.obstacle_group = []

    def set_obstacle_group(self, groups):
        self.obstacle_group = groups

    def move(self, dt):
        raise NotImplementedError

    def check_collision(self, direction):
        #print(self.obstacle_group)
        if direction == DIR_HORIZONTAL:
            for sprite in self.obstacle_group:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.is_moving_right():
                        self.hitbox.right = sprite.hitbox.left
                        print("collide right")
                    if self.is_moving_left():
                        self.hitbox.left = sprite.hitbox.right
                        print("collide left")
        if direction == DIR_VERTICAL:
            for sprite in self.obstacle_group:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.is_moving_down():
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.is_moving_up():
                        self.hitbox.top = sprite.hitbox.bottom

    def is_moving_right(self):
        return self._direction.x > 0

    def is_moving_left(self):
        return self._direction.x < 0

    def is_moving_up(self):
        return self._direction.y < 0

    def is_moving_down(self):
        return self._direction.y > 0

    def is_moving(self):
        return self._direction.magnitude() != 0

    def is_moving_vertically(self):
        return self.is_moving_up() or self.is_moving_down()

    def is_moving_horizontally(self):
        return self.is_moving_right() or self.is_moving_left()
