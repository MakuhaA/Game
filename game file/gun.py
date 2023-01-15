import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen):
        # инициализация пушки
        super(Gun, self).__init__()
        self.screen = screen
        self.im = pygame.image.load('../image/gun.png')
        self.image = pygame.image.load('../image/heart1.png')
        self.rect = self.im.get_rect()
        self.rect2 = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.right = False
        self.left = False

    def update_gun(self):
        # обновление позиции пушки
        if self.right and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.left and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        # размещение пушки по центру внизу экрана
        self.center = self.screen_rect.centerx

    def output(self):
        # рисование пушки
        self.screen.blit(self.im, self.rect)
