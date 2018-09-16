import sys
import pygame
from Alien_game_setting import Settings
from Alien_ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    bg_color = (230, 230, 230)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)
        for event in pygame.event.get():
            screen.fill(ai_setting.bg_color)
            ship.blitme()
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
run_game()
