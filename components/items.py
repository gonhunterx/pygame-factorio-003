import pygame as py 

class Item:
    def __init__(self, name, quantity=1):
        super().__init__()
        self.name = name
        self.quantity = quantity
        self.image = py.image.load(f"assets/{name.lower()}.png") 

class Coal(Item, py.sprite.Sprite):
    def __init__(self):
        Item.__init__(self, 'Coal')
        self.image = py.transform.scale(py.image.load("assets/coal.png").convert(), (32, 32))
        self.image.set_colorkey((0,0,0))

class CoalVein(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = 'Coal Vein'
        self.image = py.transform.scale(py.image.load("assets/coal_rock.png").convert(), (32, 32))
        self.image.set_colorkey((0, 0, 0))
        self.amount_of_coal = 500
        self.rect = self.image.get_rect()

    def mine(self):
        if self.amount_of_coal > 0:
            self.amount_of_coal -= 1
            return Coal()
        else:
            # right now they can just stay there even if empty 
            return None 

class IronBar(Item, py.sprite.Sprite):
    def __init__(self):
        Item.__init__(self, 'Iron-bar')
        self.image = py.transform.scale(py.image.load("assets/iron-bar.png").convert(), (32, 32))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
    
    
class rawIronOre(Item, py.sprite.Sprite):
    def __init__(self):
        Item.__init__(self, 'rawIronOre')
        self.image = py.transform.scale(py.image.load("assets/rawironore.png").convert(), (32, 32))
        self.image.set_colorkey((0,0,0))


class IronOre(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = 'rawIronOre'
        self.image = py.transform.scale(py.image.load("assets/iron_stone.png").convert(), (32, 32))
        self.image.set_colorkey((0, 0, 0))
        self.amount_of_iron = 500
        self.rect = self.image.get_rect()
    
    def mine(self):
        if self.amount_of_iron > 0:
            self.amount_of_iron -= 1
            return rawIronOre()
        else:
            return None