import random
from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite
class PowerUp(Sprite):
    def __init__(self,image,type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(125,175)

        self.start_time = 0
        self.withd = self.image.get_width() #obtenemos la posicion de la imgaen


    def update(self,game_speed,power_ups):
        self.rect.x -= game_speed
        
        if self.rect.x < -self.rect.width:
            power_ups.pop() 
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)