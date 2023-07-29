import pygame

from IMovableSprite import IMovableSprite, DIR_HORIZONTAL, DIR_VERTICAL


class IMouseMovable(IMovableSprite):
    def __init__(self, groups, pos, res_dir, min_speed=-1, max_speed=-1, delta_speed=-1):
        super().__init__(groups, pos, res_dir)
        if min_speed > 0:
            self.min_speed = min_speed
        if max_speed > 0:
            self.max_speed = max_speed
        if delta_speed > 0:
            self.delta_speed = delta_speed

    def move(self, dt):
        self._target = pygame.Vector2(pygame.mouse.get_pos()) - self.half_screen + self._pos
        move = self._direction = self._target - self._pos
        move_length = move.length()
        if self._prev_target[0] != self._target[0] and self._prev_target[1] != self._target[1]:
            self.speed = self.min_speed

        if move_length < self.speed:
            self._pos = self._target
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.speed * dt
            print(move)
            self.speed = int(pygame.math.clamp(self.speed + self.delta_speed, self.min_speed, self.max_speed))
        self._prev_target = self._target

        self.hitbox.centerx += move.x
        self.check_collision(DIR_HORIZONTAL)
        self.hitbox.centery += move.y
        self.check_collision(DIR_VERTICAL)
        self.rect.center = self.hitbox.center
        self._pos = self.rect.center
        # self.rect.center = list(int(v) for v in self._pos)
        # Debug.d(self.speed)
