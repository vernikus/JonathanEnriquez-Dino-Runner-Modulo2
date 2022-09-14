import random

from dino_runner.components.obstacles.obstacle import Obstacle


class CactusSmall(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type) #Llama a Obstacle y los pasa como paremetros
        self.rect.y = 325 

class CactusLarge(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type) #Llama a Obstacle y los pasa como paremetros
        self.rect.y = 300 


        
         
