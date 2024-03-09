import pygame as py 
from sys import exit 
from components.messageLog import MessageLog
from settings import *
from components.player import Player
from components.items import IronOre, IronBar
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
furnace_group = py.sprite.Group()
processed_resources_group = py.sprite.Group()

# Creating instances of resources and adding them to the groups
iron_ore1 = IronOre()
iron_ore2 = IronOre()
coal_vein1 = CoalVein()
coal_vein2 = CoalVein()
iron_bar = IronBar()

all_resources.add(iron_ore1, iron_ore2, coal_vein1, coal_vein2)
iron_ore_group.add(iron_ore1, iron_ore2)
coal_vein_group.add(coal_vein1, coal_vein2)
buildings_group.add(factory)
furnace_group.add(furnace)

processed_resources_group.add(iron_bar)

# Positioning resources
iron_ore1.rect.topleft = (50, 50)
iron_ore2.rect.topleft = (500, 200)
coal_vein1.rect.topleft = (500, 350)
coal_vein2.rect.topleft = (550, 280)

while True:
    collided_with_resource = py.sprite.spritecollide(player, all_resources, False)

    furnace.display_internal_resources(window)
    
    delta_time = clock.tick(FPS) / 1000.0
    keys = py.key.get_pressed()
    cursor_pos = py.mouse.get_pos()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
            
    if keys[py.K_f] and collided_with_resource:
        player.is_mining = True
        player.mine()
        current_time = py.time.get_ticks()
        if current_time - player.last_mine_time >= MINE_DELAY:
            collided_sprites = py.sprite.spritecollide(player, all_resources, False)
            # add pick axe swing animation 
            for sprite in collided_sprites:

                if isinstance(sprite, CoalVein):
                    coal = sprite.mine()
                    if coal is not None:
                        player.inventory.add_item(coal)
                elif isinstance(sprite, IronOre):
                    rawIron = sprite.mine()
                    player.mine()
                    # LOGIC MISTAKE HERE (not checking right attribute maybe)
                    if rawIron is not None:
                        player.inventory.add_item(rawIron)
            player.last_mine_time = current_time
    
    # furnace logic 

    
        # current_time = py.time.get_ticks()
        # if current_time - player.last_mine_time >= MINE_DELAY:
            # Check if the cursor is over any furnace in the furnace_group
            # for furnace in furnace_group:
            
    if furnace.rect.collidepoint(cursor_pos):  # Check if cursor is over the furnace
        if keys[py.K_e]:
            iron_ore_count, coal_count = player.inventory.count_items()
            # Only proceed if the cursor is over the furnace
            furnace.amount_of_iron_ore += iron_ore_count
            furnace.amount_of_coal += coal_count

            player.inventory.remove_item('Coal', quantity=coal_count)
            player.inventory.remove_item('rawIronOre', quantity=iron_ore_count)
            player.message_log.add_message(f'{coal_count} coal added to furnace')
            player.message_log.add_message(f'{iron_ore_count} iron added to furnace')
                    
                        # print(furnace.amount_of_coal)
                        # print(furnace.amount_of_iron_ore)
                        
                # player.last_mine_time = current_time
    # if player.rect.colliderect(factory.rect):
    #     player.pos[1] += player.pos[1] - 200
    #     player.pos[0] -= player.pos[0] + 200
        
    while furnace.has_fuel:
        furnace.process_resources()
        
     
    # if furnace.amount_of_coal and furnace.amount_of_iron_ore > 0:
    #     for _ in range(furnace.amount_of_iron_ore):
    #         furnace.process_resources()
    #         print(f"iron bars:  {furnace.amount_of_iron_bar}")    
    #         player.inventory.add_item(iron_bar)
    
        
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
    
    # MESSAGE LOG 
    player.message_log.draw(window)

    
    player.inventory.draw(window)
    player.update(buildings_group, all_resources, furnace_group, delta_time)
    
    py.display.update()
    clock.tick(FPS)