import sys
import pygame.image
from pygame import *
from basegame import run

init()

size = (720, 800)

screen = display.set_mode(size)
pygame.display.set_caption('Ship Rescue')
font_name = pygame.font.Font('../type/type2.otf', 66)
fon_image = pygame.image.load('../image/menu1.jpg')
font_menu = font.SysFont('../type/type2.otf', 50)
bg_sound = pygame.mixer.Sound('../sound/soundtrack.mp3')
bg_sound.set_volume(0.1)
bg_sound.play(-1)


class Menu:
    def __init__(self):
        self.option_surfaces = []
        self.callbacks = []
        self.current_option_index = 0

    def append_option(self, option, callback):
        self.option_surfaces.append(font_menu.render(option, True, (225, 225, 225)))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.current_option_index = max(0, min(self.current_option_index + direction,
                                               len(self.option_surfaces) - 1))

    def select(self):
        self.callbacks[self.current_option_index]()

    def draw(self, surf, x, y, option_padding):
        render_name = font_name.render('Ship Rescue', True, pygame.Color(37, 9, 104))
        screen.blit(render_name, (30, 20))
        for i, option in enumerate(self.option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x - 40, y + 30 + i * option_padding)
            if i == self.current_option_index:
                draw.rect(surf, (0, 110, 0), option_rect)
            surf.blit(option, option_rect)


menu = Menu()
menu.append_option('Start', lambda: run())
menu.append_option('Quit', quit)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                menu.switch(-1)
            elif event.key == pygame.K_s:
                menu.switch(1)
            elif event.key == K_SPACE:
                menu.select()

    screen.blit(fon_image, (0, 0))
    menu.draw(screen, 90, 90, 75)
    display.flip()
quit()
