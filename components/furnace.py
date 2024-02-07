import pygame as py 

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
        