
import pygame.sprite


class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups:  pygame.sprite.Group | list, pos=(0, 0), res_dir=''):
        if groups is None:
            groups = []
        super().__init__(*groups)
        self.surface = pygame.display.get_surface()
        self.half_screen = pygame.Vector2(self.surface.get_size()[0] // 2,
                                          self.surface.get_size()[1] // 2)
        self.image = None
        self.rect = None
        if res_dir.strip().__len__() != 0:
            self.image = pygame.image.load(res_dir).convert_alpha()
            self.rect = self.image.get_frect(topleft=pos)
        self.hitbox = self.rect.inflate(-10, -10)  # center is the same

    def update(self, dt=1):
        ...


class VisibleSprites(pygame.sprite.Group):  # YSortCameraGroup
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.half_screen = pygame.Vector2(self.surface.get_size()[0] // 2,
                                          self.surface.get_size()[1] // 2)
        self.player_sprite = None

    def draw(self, surface):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            # offset = pygame.Vector2()
            offset = (
                    pygame.Vector2(*self.player_sprite.rect.center) - self.half_screen)
            surface.blit(sprite.image, sprite.rect.topleft - offset)


class ObstacleSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
