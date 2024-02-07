import pygame as py 
from settings import * 

class MessageLog:
    def __init__(self, max_messages=5):
        self.messages = []
        self.max_messages = max_messages
        
    def add_message(self, message):
        self.messages.append(message)
        if len(self.messages) > self.max_messages:
            self.messages.pop(0) # remove oldest message 
    
    def draw(self, window):
        for i, message in enumerate(reversed(self.messages)):
            label = font.render(message, True, (0,0,0))
            window.blit(label, (10, window_h - (i+1)*20))