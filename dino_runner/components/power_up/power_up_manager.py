import random
import pygame

from dino_runner.components.power_up.shield import Shield


class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.duration = random.randint(3,6)

    def generator_power_ups(self,score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200,300)
            self.power_ups.append(Shield())

    def update(self,score,game_speed,player):
        self.generator_power_ups(score,)
        for power_up in self.power_ups:
            power_up.update(game_speed,self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.has_power_up = True
                player.type = power_up.type
                player.power_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200,300)
