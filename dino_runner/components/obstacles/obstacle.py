from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite

class Obstacle(Sprite): # Se hace la herencia de sprites
    def __init__(self, imagen, obstacle_type, ):
        self.image = imagen
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def uptade(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop() #pop elimina al elemento 

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type],(self.rect.x,self.rect.y))


