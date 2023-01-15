import pygame
import sys
from bullet import Bullet
from siren import Siren
import time


def events(screen, gun, bullets):
    # обработка клавиш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.right = True
            elif event.key == pygame.K_a:
                gun.left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.right = False
            elif event.key == pygame.K_a:
                gun.left = False


def update(backround, screen, stat, score, gun, many_siren, bullets):
    # обновление экрана
    screen.blit(backround, (0, 0))
    # screen.fill(overlay)
    score.show_res()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    many_siren.draw(screen)
    pygame.display.flip()


def update_bullet(screen, stat, score, many_siren, bullets):
    # обновление позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, many_siren, True, True)
    if collisions:
        for many_siren in collisions.values():
            stat.score += 10 * len(many_siren)
        stat.score += 10
        score.res()
        check_score(stat, score)
        score.image_hearts()
    if len(many_siren) == 0:
        bullets.empty()
        creat_army(screen, many_siren)


def update_siren(stat, screen, score, gun, many_siren, bullets):
    # обновляет позицию сирен
    many_siren.update()
    if pygame.sprite.spritecollideany(gun, many_siren):
        kill(stat, screen, score, gun, many_siren, bullets)
    siren_check(stat, screen, score, gun, many_siren, bullets)


def kill(stat, screen, score, gun, many_siren, bullets):
    # столкновение пушки и армии
    if stat.live > 0:
        stat.live -= 1
        score.image_hearts()
        many_siren.empty()
        bullets.empty()
        creat_army(screen, many_siren)
        gun.create_gun()
        time.sleep(1)
    else:
        backround = pygame.image.load('../image/ship1.jpg')
        screen.blit(backround, (0, 0))
        font_end = pygame.font.SysFont('../type/type2.otf', 90, bold=True)
        render_end = font_end.render('GAME OVER', True, pygame.Color('violet'))
        screen.blit(render_end, (720 // 2 - 200, 720 // 3))
        pygame.display.flip()
        time.sleep(2)
        stat.run_game = False
        sys.exit()


def siren_check(stat, screen, score, gun, many_siren, bullets):
    # проверка, добралась ли армия до края экрана
    screen_rect = screen.get_rect()
    for siren in many_siren.sprites():
        if siren.rect.bottom >= screen_rect.bottom:
            kill(stat, screen, score, gun, many_siren, bullets)
            break


def creat_army(screen, many_siren):
    # создание армии сирен
    siren = Siren(screen)
    siren_width = siren.rect.width
    n_siren_x = int((750 - 2 * siren_width) / siren_width)
    siren_height = siren.rect.height
    n_siren_y = int((800 - 100 - 2 * siren_height) / siren_height)
    for row_n in range(n_siren_y - 1):
        for penny_1 in range(n_siren_x + 1):
            siren = Siren(screen)
            siren.x = siren_width + siren_width * penny_1
            siren.y = siren_height + siren_height * row_n
            siren.rect.x = siren.x
            siren.rect.y = siren.rect.height + siren.rect.height * row_n
            many_siren.add(siren)


def check_score(stat, score):
    # проверка новых рекордов
    if stat.score > stat.score_high:
        stat.score_high = stat.score
        score.high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stat.score_high))
