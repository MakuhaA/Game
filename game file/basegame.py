import pygame
import control
from gun import Gun
from pygame.sprite import Group
from stats import Stat
from score import Score


def run():
    pygame.init()
    screen = pygame.display.set_mode((720, 800))
    gun = Gun(screen)
    pygame.display.set_caption('Ship Rescue')
    #overlay = (0, 0, 0)
    backround = pygame.image.load('../image/ship1.jpg')
    # overlay = pygame.image.load('![](../image/ship.jpg)')
    bullets = Group()
    many_siren = Group()
    control.creat_army(screen, many_siren)
    stat = Stat()
    score = Score(screen, stat)

    while True:
        control.events(screen, gun, bullets)
        if stat.run_game:
            gun.update_gun()
        gun.update_gun()
        control.update(backround, screen, stat, score, gun, many_siren, bullets)
        control.update_bullet(screen, stat, score, many_siren, bullets)
        control.update_siren(stat, screen, score, gun, many_siren, bullets)



