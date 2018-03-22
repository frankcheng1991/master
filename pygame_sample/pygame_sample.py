# -*- coding: utf-8 -*-
# pygame sample

#---------------------------- import modules ------------------------#

import pygame

#-------------------------- game initialization ---------------------#

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Sample game")

# icon = pygame.image.load("image.png")
# pygame.display.set_icon("icon")

#------------------------------ define color ---------------------#
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)

#------------------------------ define Variables ---------------------#
display_width = 800
display_height = 600

FPS = 10
clock = pygame.time.Clock()

#------------------------------ define Font ---------------------#
smallFont = pygame.font.SysFont("comicsansms", 25)
midFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)
# font = pygame.font.Font("myresources/fonts/Papyrus.ttf", 26) # this is to import font from outside

#------------------------------ define Functions ---------------------#
def text_objects(msg, color, size):
	if size == "small":
		textSurface = smallFont.render(msg, True, color)
	elif size == "medium":
		textSurface = midFont.render(msg, True, color)
	elif size == "large":
		textSurface = largeFont.render(msg, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size = "small"):
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = (display_width / 2), (display_height / 2) + y_displace
	gameDisplay.blit(textSurf, textRect)


def pause():
	pause = True
	message_to_screen("Paused", black, -100, size = "large")
	message_to_screen("Press C to continue, Q to quit!", black, 25)
	pygame.display.update()
	
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_c:
					pause = False

def game_intro():
	intro = True
	gameDisplay.fill(white)
	message_to_screen("Welcome to sample game!", green, -100, "large")
	message_to_screen("The objects of the game is to eat red apples", black, -30)
	message_to_screen("The more apples you eat, the longer you get", black, 10)
	message_to_screen("If you run into yourself, or the edges, you die!", black, 50)
	message_to_screen("Press C to play or Q to quit or P to pause", black, 180)
	pygame.display.update()

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_c:
					intro = False

#------------------------------ main game loop ---------------------#
def gameLoop():

	gameDisplay.fill(white)

	# set local or global variables that need to change each loop
	gameExit = False
	gameOver = False

	
	while not gameExit:
		if gameOver == True:
			message_to_screen("Game Over", red, y_displace = -50, size = "large")
			message_to_screen("Press C to continue or Q to quit!", black, y_displace = 50, size = "medium")
			pygame.display.update()
		while gameOver:
			message_to_screen("Game Over", red, y_displace = -50, size = "large")
			message_to_screen("Press C to continue or Q to quit!", black, y_displace = 50, size = "medium")
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = True
					elif event.key == pygame.K_c:
						gameLoop()

		# core game engine here
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameExit = True
				elif event.key == pygame.K_p:
					pause()

		pygame.display.update()
		clock.tick(FPS) # control the refresh rate

	pygame.display.update()
	pygame.quit()
	quit()

#------------------------------ main function ---------------------#
if __name__ == "__main__":
	game_intro()
	gameLoop()