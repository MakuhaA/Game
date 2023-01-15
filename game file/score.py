import pygame.font
from gun import Gun
from pygame.sprite import Group


class Score():
    def __init__(self, screen, stat):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stat = stat
        self.text_color = (225, 225, 225)
        self.font = pygame.font.SysFont('../type/type2.otf', 26, bold=True)
        self.res()
        self.high_score()
        self.image_hearts()

    def res(self):
        self.res_score = self.font.render(str(self.stat.score), True, self.text_color)
        self.score_rect = self.res_score.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.score_rect.top = 20

    def high_score(self):
        self.im_high_score = self.font.render(
            str(self.stat.score_high), True, self.text_color)
        self.high_score_rect = self.im_high_score.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_hearts(self):
        self.hearts = Group()
        for heartn in range(self.stat.live):
            heart = Gun(self.screen)
            heart.rect.x = 15 + heartn * heart.rect2.width
            heart.rect.y = 20
            self.hearts.add(heart)

    def show_res(self):
        self.screen.blit(self.res_score, self.score_rect)
        self.screen.blit(self.im_high_score, self.high_score_rect)
        self.hearts.draw(self.screen)
