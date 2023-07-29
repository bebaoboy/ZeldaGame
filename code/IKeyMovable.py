import pygame

from IMovableSprite import IMovableSprite, DIR_HORIZONTAL, DIR_VERTICAL


class IKeyMovable(IMovableSprite):
    def __init__(self, groups, pos, res_dir, min_speed=-1, max_speed=-1, delta_speed=-1):
        super().__init__(groups, pos, res_dir)
        if min_speed > 0:
            self.min_speed = min_speed
        if max_speed > 0:
            self.max_speed = max_speed
        if delta_speed > 0:
            self.delta_speed = delta_speed

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self._direction.y = -1
        elif keys[pygame.K_DOWN]:
            self._direction.y = 1
        else:
            self._direction.y = 0

        if keys[pygame.K_RIGHT]:
            self._direction.x = 1
        elif keys[pygame.K_LEFT]:
            self._direction.x = -1
        else:
            self._direction.x = 0

        if self._direction.magnitude() != 0:
            self._direction.normalize()
        # self.rect.center += self._direction * int(self.speed * dt)
        self.hitbox.centerx += self._direction.x * int(self.speed * dt)
        self.check_collision(DIR_HORIZONTAL)
        self.hitbox.centery += self._direction.y * int(self.speed * dt)
        self.check_collision(DIR_VERTICAL)
        self.rect.center = self.hitbox.center
        # print(self._direction)
        # print(self._direction * self.speed * dt)
        # print(self.rect.center)
