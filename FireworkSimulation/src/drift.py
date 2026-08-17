from settings import *
import random
import pygame

class Drift:

    def __init__(self, height, pos_x, screen):
        self.height = height
        self.pos_x = pos_x
        self.steps = 0.0
        self.count = 0
        self.screen = screen
        self.drift = [0.0]*MAX_LENGTH
        self.color = [200, 200, 200]

    def draw(self):
        for i in range(MAX_LENGTH):
            if self.steps-i*PIXEL_SIZE < SCREEN_SIZE_Y-self.height:
                if (not i in range(MAX_LENGTH-9, MAX_LENGTH)
                    or (i in range(MAX_LENGTH-9, MAX_LENGTH) and random.randint(0, 2) == 0)):
                    pygame.draw.rect(self.screen, self.color,
                                        [self.pos_x-PIXEL_SIZE/2+self.drift[i],
                                        SCREEN_SIZE_Y-self.steps+i*PIXEL_SIZE,
                                        PIXEL_SIZE, PIXEL_SIZE])

    def update_drift(self):
        for i in range(MAX_LENGTH):
            l = random.randint(1, 5)
            while not l <= MAX_LENGTH-i:
                l = random.randint(1, 5)
            for s in range(l):
                self.drift[i+s] = random.randint(-1, 1)
    
    def is_finished(self):
        return self.steps - MAX_LENGTH * PIXEL_SIZE >= SCREEN_SIZE_Y - self.height
    
    def update(self):
        if self.count < 8:
            self.count += 1
        else:
            self.count = 0
            self.update_drift()
        if self.steps-MAX_LENGTH*PIXEL_SIZE < SCREEN_SIZE_Y-self.height:
            self.steps += ROCKET_SPEED
        self.draw()