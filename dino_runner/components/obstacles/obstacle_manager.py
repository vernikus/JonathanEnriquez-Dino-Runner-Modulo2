import pygame
import random
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.cactus import CactusSmall
from dino_runner.components.obstacles.cactus import CactusLarge
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self,game):
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                cactus = CactusSmall(SMALL_CACTUS) #Se crae la instancia de cactus
                self.obstacles.append(cactus)
            elif random.randint(0,2) == 1:
                cactus = CactusLarge(LARGE_CACTUS)          
                self.obstacles.append(cactus)
            elif random.randint(0,2) == 2:
                bird = Bird(BIRD)          
                self.obstacles.append(bird)
        for obstacle in self.obstacles:
            obstacle.uptade(game.game_speed,self.obstacles)
            # if game.player.dino_rect.colliderect(obstacle.rect):
            #     game.playing = False
            #     break
            #     pygame.time.delay(1000)

    def draw(self,screen):
        for obstacle in self.obstacles: #Recoremos la lista
            obstacle.draw(screen) 