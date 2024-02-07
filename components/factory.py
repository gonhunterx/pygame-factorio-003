import pygame as py 

class Factory(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.transform.scale(py.image.load("assets/factory.png").convert(), (128, 128))
        self.image.set_colorkey((0,0,0))
        self.research_rate = 20
        self.unlock_price = 1000
        self.pos = py.math.Vector2((200, 200))
        self.rect = self.image.get_rect(topleft=self.pos)