import pygame
# need system to break the program
from hero import Hero
from settings import Settings
from game_functions import check_events
from pygame.sprite import Group, groupcollide
from enemy import Enemy
from button import Start_Button
import os

game_settings = Settings()
# itit al of the pygame modules
pygame.init()
screen = pygame.display.set_mode(game_settings.screen_size)

hero_group = Group()
hero = Hero(screen, game_settings)
hero_group.add(hero)
# make a backgroung color
# put a message on the status bar so the platyer knows the name of the game
pygame.display.set_caption("Recruiter Attack!!")
enemies = Group()
enemies.add(Enemy(screen,game_settings))

# make a start button
start_button = Start_Button(screen)

# this loop will run forever...
while 1:
	check_events(hero, start_button, game_settings)
	screen.fill(game_settings.bg_color)
	for hero in hero_group.sprites():
		if game_settings.game_active:
			hero.update_me()
		hero.draw_me()
	for enemy in enemies.sprites():
		if game_settings.game_active:
			enemy.update_me(hero)
		enemy.draw_me()
	hero_died = groupcollide(hero_group, enemies, True, True)
	if hero_died:
		print "you are the new President of the United States!!!!"
		os.system("say --voice=Milena 'You are now the president of the united states'")
		game_settings.game_active == False
	if game_settings.game_active == False:
		start_button.draw_button()
	pygame.display.flip()



