import pygame

from IMovableSprite import IMovableSprite, DIR_HORIZONTAL, DIR_VERTICAL


class IFollowUp(IMovableSprite):
    def __init__(self, groups, pos, res_dir):
        super().__init__(groups, pos, res_dir)
        self.lerp_factor = 0.01
        self.minimum_distance = 1.0
        self.maximum_distance = 1000.0

    def move(self, dt):
        follower_vector = new_follower_vector = pygame.Vector2(self.hitbox.center)
        self._target = pygame.Vector2(pygame.mouse.get_pos()) - self.half_screen + follower_vector

        distance = follower_vector.distance_to(self._target)
        if distance > self.minimum_distance:
            direction_vector = (self._target - follower_vector) / distance
            min_step = max(self.minimum_distance, distance - self.maximum_distance)
            max_step = distance - self.minimum_distance
            step_distance = min_step + (max_step - min_step) * self.lerp_factor * dt
            new_follower_vector = follower_vector + direction_vector * int(step_distance)
            self._direction = new_follower_vector - self.hitbox.center
            print(self._direction)
            # if abs(self._direction.x) > self.max_speed * 2 or abs(self._direction.y) > self.max_speed * 2:
            #     self.hitbox.center = self._target
            #     print("jump" + str(self.hitbox.center) + "to" + str(self._target))
            #     return
            self.hitbox.centerx += new_follower_vector.x - self.hitbox.centerx
            self.check_collision(DIR_HORIZONTAL)
            self.hitbox.centery += new_follower_vector.y - self.hitbox.centery
            self.check_collision(DIR_VERTICAL)
            self.rect.center = self.hitbox.center

        # self.rect.center = (new_follower_vector.x, new_follower_vector.y)
