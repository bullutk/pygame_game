import pygame
# need system to break the program
from hero import Hero
import sys
import os
from settings import Settings

game_settings = Settings()
# itit al of the pygame modules
pygame.init()
screen = pygame.display.set_mode(game_settings.screen_size)
hero = Hero(screen, game_settings)
# make a backgroung color
# put a message on the status bar so the platyer knows the name of the game
pygame.display.set_caption("Recruiter Attack!!")

# this loop will run forever...
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# check for keypress
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = True
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True
			elif event.key == pygame.K_UP:
				hero.moving_up = True
			elif event.key == pygame.K_DOWN:
				hero.moving_down = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = False
			elif event.key == pygame.K_LEFT:
				hero.moving_left = False
			elif event.key == pygame.K_UP:
				hero.moving_up = False
			elif event.key == pygame.K_DOWN:
				hero.moving_down = False



	screen.fill(game_settings.bg_color)
	hero.update_me()
	hero.draw_me()
	pygame.display.flip()



