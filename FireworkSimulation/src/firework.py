from settings import *
from colors import COLOR_PALETTES
import pygame
import random
import math

class Firework:
    
    def __init__(self, height, pos_x, screen):
        self.height = height
        self.pos_x = pos_x
        self.steps = 0.0
        
        self.red, self.green, self.blue = random.choice(COLOR_PALETTES)
        self.brightness = 1.0
        
        self.firework = [(0.0, 0.0)]*PIXEL_NUMBER
        self.screen = screen
        self.update_firework()

    def draw(self):
        for i in range(PIXEL_NUMBER):
            x, y = self.firework[i]
            pygame.draw.rect(self.screen, [int(self.red*self.brightness),
                                      int(self.green*self.brightness),
                                      int(self.blue*self.brightness)],
                                [self.pos_x-PIXEL_SIZE/2+x*self.steps,
                                self.height-PIXEL_SIZE/2+y*self.steps,
                                PIXEL_SIZE, PIXEL_SIZE])
    
    def is_finished(self):
        return self.brightness <= 0
    
    def update_firework(self):
        r = random.randint(MAX_RADIUS-30, MAX_RADIUS)
        for i in range(PIXEL_NUMBER):
            angle = random.uniform(0, 2 * math.pi)
            dist = r * math.sqrt(random.random())
            self.firework[i] = (math.cos(angle) * dist, math.sin(angle) * dist)
    
    def update(self):
        if self.steps < 1:
            self.steps += EXPLOSION_SPEED
        else:
            if not self.brightness <= 0:
                self.brightness -= EXPLOSION_SPEED
        self.draw()