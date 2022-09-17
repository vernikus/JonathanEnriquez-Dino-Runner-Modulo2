import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_up.power_up_manager import PowerUpManager

from dino_runner.utils.constants import BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS ,FONT_STYLE,HAMMER_TYPE
from dino_runner.components.dinosaur import Dinosaur


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_maganer = PowerUpManager()
        self.runnig = False
        self.score = 0
        self.death_count = 0
        self.list_score = []

    def execute(self):
        self.runnig = True
        while self.runnig:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.uptade_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_maganer.update(self.score,self.game_speed,self.player,user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_maganer.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runnig = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.list_score.append(self.score)
                
                self.run()
    
    def reset_game(self):
        self.score = 0
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()
        self.power_up_maganer.reset_power_ups()

    def uptade_score(self):
        self.score += 1
        if self.score % 100 == 0 and self.game_speed < 600:
            self.game_speed += 5 #En cada multiplo de 100 se aumenta la velocidad del juego

    def draw_score(self):
        self.generator_text(f'Score:{self.score}',(0,250,0),1000,50,0)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/ 1000 ,2)
            if time_to_show >= 0:
                if self.player.type == HAMMER_TYPE:
                    self.generator_text(f'Press space to use a hammer',(0,0,250),500,50,0)
                elif self.player.type == SHIELD_TYPE:
                    self.generator_text(f'{self.player.type.capitalize()} enabled for {time_to_show} seconds',(0,0,250),500,50,0)
            else:
                self.player.has_power_up = False#####
                self.player.type = DEFAULT_TYPE    
      

    def show_menu(self):
        self.screen.fill((255,255,255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            self.generator_text('Press any key to start..',(200,0,0),half_screen_width,half_screen_height,0)
        else:
            self.generator_text(f'Game over total deahts: {self.death_count}',(200,0,0),half_screen_width,half_screen_height,0)
            self.generator_text(f'Press any key ... ',(200,0,0),half_screen_width,half_screen_height,30)
            self.generator_text(f'Total score: {self.score}',(200,0,0),half_screen_width,half_screen_height,60)
        self.screen.blit(ICON,(half_screen_width-20,half_screen_height-140))
        pygame.display.update()
        self.handle_events_on_menu()

    
    def generator_text(self,text_to_generate,color_text,pos_x,pos_y,difference):
        font = pygame.font.Font(FONT_STYLE,30)
        text = font.render(text_to_generate,True,(color_text) ) #(texto,anti-area,color)
        text_rec = text.get_rect()
        text_rec.center = (pos_x,pos_y + difference) #centramos el texto
        self.screen.blit(text, text_rec)