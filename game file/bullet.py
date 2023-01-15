import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('../image/bullet.png')
        self.rect = self.image.get_rect()
        self.color = 127, 127, 127
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # перемещение пули
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
