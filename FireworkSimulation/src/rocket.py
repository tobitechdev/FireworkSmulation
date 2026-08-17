from drift import Drift
from firework import Firework

class Rocket:
    
    def __init__(self, height, pos_x, screen, explosion_sound):
        self.height = height
        self.pos_x = pos_x
        self.step = 0
        self.drift = Drift(height, pos_x, screen)
        self.firework = Firework(height, pos_x, screen)
        self.screen = screen
        self.explosion_sound = explosion_sound
        self.exploded = False
    
    def is_finished(self):
        return self.drift.is_finished() and self.firework.is_finished()
    
    def update(self):
        if self.drift.is_finished() == False:
            self.drift.update()
        else:
            if not self.exploded:
                self.explosion_sound.play()
                self.exploded = True
            self.firework.update()