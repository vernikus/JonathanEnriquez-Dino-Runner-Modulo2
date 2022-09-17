import pygame
from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE,HAMMER,HAMMER_TYPE, DEFAULT_TYPE, HAMMER





class Shield(PowerUp):
    def __init__(self,):
        super().__init__(SHIELD,SHIELD_TYPE)

class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.hamer_rect = self.image.get_rect()
        # self.hamer_rect.x = 80
        # self.hamer_rect.y = 310
        super().__init__(HAMMER,HAMMER_TYPE)
            
        
    def shoot_hammer(self,user_input,player):
        if user_input[pygame.K_SPACE]:
            player.type = DEFAULT_TYPE
            
            print('atack')   
# class Shield(PowerUp):
#     POWER_UPS = {
#         'SHIELD':(SHIELD, SHIELD_TYPE),
#         'HAMMER':(HAMMER,HAMMER_TYPE)
#     }
#     def __init__(self,power_up_type):        
#         image,image_type = self.POWER_UPS[power_up_type]
#         super().__init__(image,image_type)
            
