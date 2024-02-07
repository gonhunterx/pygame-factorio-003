import pygame as py 
from sys import exit 
from components.messageLog import MessageLog
from settings import *
from components.player import Player
from components.items import IronOre
from components.items import CoalVein
from components.factory import Factory
from components.furnace import Furnace 

py.init()

window = py.display.set_mode((window_w, window_h))
py.display.set_caption("Factory MMO")
clock = py.time.Clock()

# MIXER 
py.mixer.init()
py.mixer.music.load("audio/SwitchWithMeTheme.wav")
# audio settings
py.mixer.music.set_volume(0.1)
py.mixer.music.play(-1)

# loads images 
background = py.transform.scale(py.image.load("assets/world_map.png").convert(), (window_w, window_h))


player = Player()
factory = Factory()
furnace = Furnace()
message_log = MessageLog()


# Creating resource groups
all_resources = py.sprite.Group()
iron_ore_group = py.sprite.Group()
coal_vein_group = py.sprite.Group()
buildings_group = py.sprite.Group()

# Creating instances of resources and adding them to the groups
iron_ore1 = IronOre()
iron_ore2 = IronOre()
coal_vein1 = CoalVein()
coal_vein2 = CoalVein()

all_resources.add(iron_ore1, iron_ore2, coal_vein1, coal_vein2)
iron_ore_group.add(iron_ore1, iron_ore2)
coal_vein_group.add(coal_vein1, coal_vein2)
buildings_group.add(factory)
# Positioning resources
iron_ore1.rect.topleft = (50, 50)
iron_ore2.rect.topleft = (500, 200)
coal_vein1.rect.topleft = (500, 350)
coal_vein2.rect.topleft = (550, 280)
while True:
    
    keys = py.key.get_pressed()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
            
    if keys[py.K_f]:
        current_time = py.time.get_ticks()
        if current_time - player.last_mine_time >= MINE_DELAY:
            collided_sprites = py.sprite.spritecollide(player, all_resources, False)
            for sprite in collided_sprites:
                if isinstance(sprite, CoalVein):
                    coal = sprite.mine()
                    if coal is not None:
                        player.inventory.add_item(coal)
                elif isinstance(sprite, IronOre):
                    rawIron = sprite.mine()
                    if rawIron is not None:
                        player.inventory.add_item(rawIron)
            player.last_mine_time = current_time
            
    # if player.rect.colliderect(factory.rect):
    #     player.pos[1] += player.pos[1] - 200
    #     player.pos[0] -= player.pos[0] + 200
        
    
    
    # for sprite in collided_sprites:
    #     print(f"Collided with {sprite}")

        
    all_resources.update()
    
    window.blit(background, (0,0))
    all_resources.draw(window)
    
    # objects 
    window.blit(factory.image, factory.pos)
    window.blit(furnace.image, furnace.pos)

    window.blit(iron_ore1.image, iron_ore1.rect.topleft)
    window.blit(iron_ore2.image, iron_ore2.rect.topleft)
    window.blit(coal_vein1.image, coal_vein1.rect.topleft)
    window.blit(coal_vein2.image, coal_vein2.rect.topleft)
    
    window.blit(player.current_image, player.pos)
    
    
    player.message_log.draw(window)

    
    player.inventory.draw(window)
    player.update(buildings_group, all_resources)
    
    py.display.update()
    clock.tick(FPS)