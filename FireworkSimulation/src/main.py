from settings import *
from paths import ICON, EXPLOSION_SOUND
from rocket import Rocket
import pygame

pygame.init()
pygame.mixer.init()
Icon = pygame.image.load(ICON)
pygame.display.set_icon(Icon)
screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

explosion_sound = pygame.mixer.Sound(EXPLOSION_SOUND)
explosion_sound.set_volume(SOUND_VOLUME)

rockets = []

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rockets.append(Rocket(mouse_y, mouse_x, screen, explosion_sound))

    screen.fill((0, 0, 0))
    
    for r in rockets:
        r.update()

    rockets = [r for r in rockets if not r.is_finished()]

    clock.tick(60)
    pygame.display.update()
pygame.display.quit()