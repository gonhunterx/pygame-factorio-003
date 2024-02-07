import pygame as py 
from settings import *
from components.messageLog import MessageLog
import math
from components.inventory import Inventory
from components.items import *

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.cash = 0
        self.inventory = Inventory(capacity=10)
        self.sprite_sheet = py.image.load("assets/walking_sheet.png").convert_alpha()
        self.frames = self.slice_spritesheet()
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.flipped_frames = [py.transform.flip(frame, True, False) for frame in self.frames]
        self.current_image = self.image 
        self.pos = py.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.speed = PLAYER_SPEED 
        self.rect = self.image.get_rect(topleft=self.pos)
        self.message_log = MessageLog()
        self.last_mine_time = 0
        self.prev_pos = self.pos
        
    def slice_spritesheet(self):
        frames = []
        sprite_width = 16
        sprite_height = 16
        for i in range(self.sprite_sheet.get_width() // sprite_width):
            frame = self.sprite_sheet.subsurface(py.Rect(i * sprite_width, 0, sprite_width, sprite_height))
            frames.append(py.transform.scale(frame, (32, 32)))
        return frames

    def check_resource_collision(player, resource_group):
        for resource in resource_group:
            if player.rect.colliderect(resource.rect):
                if isinstance(resource, CoalVein):
                    player.inventory.add_item(Item("Coal", 1))  # Adjust quantity as needed
                    resource.amount_of_coal -= 1  # Or any other logic for reducing resource quantity
                elif isinstance(resource, IronOre):
                    player.inventory.add_item(Item("raw Iron Ore", 1))  # Adjust quantity as needed
                    resource.amount_of_iron -= 1  # Or any other logic for reducing resource quantity

                # Optionally, remove the resource if depleted
                if resource.amount_of_coal <= 0 or resource.amount_of_iron <= 0:
                    resource.kill()

    
    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0 
        
        keys = py.key.get_pressed()
        
        if keys[py.K_w]:
            self.velocity_y = -self.speed
        if keys[py.K_a]:
            self.velocity_x = -self.speed
            self.current_image = self.flipped_frames[self.current_frame]
        if keys[py.K_s]:
            self.velocity_y = self.speed
        if keys[py.K_d]:
            self.velocity_x = self.speed 
            self.current_image = self.frames[self.current_frame]

        # player is moving diagonally 
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)
        
    def move(self):
        self.prev_pos = self.pos
        self.pos += py.math.Vector2(self.velocity_x, self.velocity_y)
        self.rect.topleft = self.pos
        self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def draw_inventory(surface, inventory):
        start_x, start_y = 10, 10  # Inventory display start position
        item_height = 20  # Height of each inventory item display
        font = py.font.Font(None, 24)  # Use pygame's default font

        for index, (item_name, item) in enumerate(inventory.items.items()):
            text_surface = font.render(f"{item_name}: {item.quantity}", True, (255, 255, 255))
            surface.blit(text_surface, (start_x, start_y + index * item_height))

        
    # INTERACTIONS WITH OBJECTS
    def update(self, buildings, resources):
        self.user_input()
    # COLLISION
        self.rect.topleft += py.math.Vector2(self.velocity_x, self.velocity_y)

        collided_with_building = py.sprite.spritecollide(self, buildings, False)
        if collided_with_building:
            self.rect.topleft -= py.math.Vector2(self.velocity_x, self.velocity_y)
            self.velocity_x = 0
            self.velocity_y = 0
            print("collided")
        
        self.move()

        collided_with_resource = py.sprite.spritecollide(self, resources, False)