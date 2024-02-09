import pygame as py 
from settings import *


# Upgrades for the inventory 
# - add it to a window of its own 
# - put the amount of an item into the corner of the icon for the item itself 


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
        # add logic here to check if adding the item exceeds the capacity

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
            
    def count_items(self):
        iron_ore_counter = 0
        coal_counter = 0
        for item_name, item in self.items.items():
            print(item_name, item.quantity)
            if item_name == 'rawIronOre':
                iron_ore_counter = item.quantity
            if item_name == 'Coal':
                coal_counter = item.quantity
        return iron_ore_counter, coal_counter  
            