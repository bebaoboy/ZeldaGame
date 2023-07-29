import pygame

from debug import Debug
from sprite import Sprite
from IMouseMovable import IMouseMovable
from IKeyMovable import IKeyMovable
from IFollowUp import IFollowUp


class Player(IKeyMovable):
    def __init__(self, groups, pos, res_dir='./graphics/test/player2.png'):
        super().__init__(groups, pos, res_dir)
        self.hitbox = self.rect.inflate(-10, -26)  # center is the same

    def update(self, dt=1):
        self.move(dt)

    # def _check_keys(self, dt):
    #     keys = pygame.key.get_pressed()
    #
    #     if keys[pygame.K_UP]:
    #         self.__direction.y = -1
    #     elif keys[pygame.K_DOWN]:
    #         self.__direction.y = 1
    #     else:
    #         self.__direction.y = 0
    #
    #     if keys[pygame.K_RIGHT]:
    #         self.__direction.x = 1
    #     elif keys[pygame.K_LEFT]:
    #         self.__direction.x = -1
    #     else:
    #         self.__direction.x = 0
    #
    #     if self.__direction.magnitude() != 0:
    #         self.__direction.normalize()
    #     self.rect.center += self.__direction * self.speed * dt
    #     print(self.__direction)
    #     print(self.__direction * self.speed * dt)
    #     print(self.rect.center)

    # def _check_mouse(self, dt):
    #     # self.rect.center =  pygame.mouse.get_pos()
    #
    #     # mouse with delay
    #
    #     self.__target = pygame.Vector2(pygame.mouse.get_pos())
    #     move = self.__target - self.__pos
    #     move_length = move.length()
    #     if self.__prev_target[0] != self.__target[0] and self.__prev_target[1] != self.__target[1]:
    #         self.speed = MIN_SPEED
    #
    #     if move_length < self.speed:
    #         self.__pos = self.__target
    #     elif move_length != 0:
    #         move.normalize_ip()
    #         move = move * self.speed
    #         self.speed = pygame.math.clamp(self.speed + self.delta_speed, MIN_SPEED, MAX_SPEED) * dt
    #         self.__pos += move
    #
    #     self.rect.center = list(int(v) for v in self.__pos)
    #     self.__prev_target = self.__target
    #     # Debug.d(self.speed)

    # def follow_me(self, dt):
    #     self.__target = pygame.Vector2(pygame.mouse.get_pos())
    #     follower_vector = new_follower_vector = pygame.Vector2(self.rect.center)
    #
    #     distance = follower_vector.distance_to(self.__target)
    #     if distance > minimum_distance:
    #         direction_vector = (self.__target - follower_vector) / distance
    #         min_step = max(1.0, distance - maximum_distance)
    #         max_step = distance - minimum_distance
    #         step_distance = min_step + (max_step - min_step) * LERP_FACTOR
    #         new_follower_vector = follower_vector + direction_vector * step_distance * dt
    #
    #     self.__direction = new_follower_vector
    #     self.rect.center = (new_follower_vector.x, new_follower_vector.y)
