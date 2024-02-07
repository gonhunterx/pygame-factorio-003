import pygame as py 
from settings import *

# INVENTORY
class Inventory:
    def __init__(self, capacity):
        self.items = {}  # Use a dictionary for easy access and management
        self.capacity = capacity
        self.font = py.font.Font(None, 36)

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item
        # Optionally, you can add logic here to check if adding the item exceeds the capacity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name].quantity -= quantity
            if self.items[item_name].quantity <= 0:
                del self.items[item_name]

    def draw(self, screen):
        x = 10
        y = 10
        for item_name, item in self.items.items():
            screen.blit(item.image, (x, y - 10))  # Blit the image onto the screen
            text = self.font.render(f": {item.quantity}", True, (255, 255, 255))
            screen.blit(text, (x + item.image.get_width(), y))  # Blit the quantity next to the image
            y += max(self.font.get_height(), item.image.get_height()) 