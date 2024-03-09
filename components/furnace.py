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
        if self.amount_of_coal >= 1 and self.amount_of_iron_ore >= 1:
            self.has_fuel = True 
        # current_time = py.time.get_ticks()
        # if current_time - self.last_process_time >= MINE_DELAY:
        if self.has_fuel:
            self.amount_of_coal -= 1
            self.amount_of_iron_ore -= 1
            self.amount_of_iron_bar += 1
            self.has_fuel = False
        return self
    
    def display_internal_resources(self, window):
        x = self.rect.x
        y = self.rect.y 

        # Create a default font
        font = py.font.Font(None, 24)

        # Create a Surface for each value
        coal_surface = font.render(str(self.amount_of_coal), True, (255, 255, 255))
        iron_ore_surface = font.render(str(self.amount_of_iron_ore), True, (255, 255, 255))

        # Draw the Surfaces
        window.blit(coal_surface, (x, y + 10))
        window.blit(iron_ore_surface, (x, y + 15))
        
    