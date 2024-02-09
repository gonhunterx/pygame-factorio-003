import pygame as py 
from settings import * 

class Furnace(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.transform.scale(py.image.load("assets/furnace.png").convert(), (64, 64))
        self.image.set_colorkey((0,0,0))
        self.pos = py.math.Vector2((600, 500))
        self.rect = self.image.get_rect(topleft=self.pos)
        self.amount_of_coal = 0
        self.amount_of_iron_ore = 0 
        self.amount_of_iron_bar = 0
        self.last_process_time = 0
        self.has_fuel = False 
        
    def process_resources(self):
        if self.amount_of_coal >= 1:
            self.has_fuel = True 
        # current_time = py.time.get_ticks()
        # if current_time - self.last_process_time >= MINE_DELAY:
        while self.has_fuel:
            self.amount_of_coal -= 1
            self.amount_of_iron_ore -= 1
            self.amount_of_iron_bar += 1
        return 
            