# -*- coding: utf-8 -*-
# pygame.py
'''
learn from youtube:
url = https://www.youtube.com/watch?v=umHZ6wnQTyQ&t=73s
# How to install pygame:
url = https://stackoverflow.com/questions/17869101/unable-to-install-pygame-using-pip
url_link = https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
'''


import pygame
import time
import random
import sys # this is for building

pygame.init() # game start, it will return a tuple to represent success and failure

gameDisplay = pygame.display.set_mode((800, 600)) # set the window size

pygame.display.set_caption('Slither') # set title of the game

img = pygame.image.load('snack_head.png')
appleimg = pygame.image.load('apple.png')
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon) # set the icon of the game, ideally to be 34 by 34

# set variables:
white = (255, 255, 255) # set RGB
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

global AppleThickness

block_size = 20 # size of snack unit! -> so the snack head is 20 by 20 rect, we can replace it with 20 by 20 image
FPS = 10

clock = pygame.time.Clock() # this is for setting frame per second

direction = 'right'

#font = pygame.font.SysFont(None, 25) # font size 25; this is the system default font
# font = pygame.font.Font(None, 25)﻿ # this is for older version of python; can use font downloaded on the Internet
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def text_objects(text, color, size):
	if size == 'small':
		textSurface = smallfont.render(text, True, color)
	elif size == 'medium':
		textSurface = medfont.render(text, True, color)
	elif size == 'large':
		textSurface = largefont.render(text, True, color)
	#textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace = 0, size = "small"): # set message box when user lose
	#screen_text = font.render(msg, True, color)
	#gameDisplay.blit(screen_text, [display_width/2, display_height/2])
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = (display_width / 2), (display_height / 2) + y_displace
	gameDisplay.blit(textSurf, textRect)

#def snack(lead_x, lead_y, block_size):
def snack(block_size, snackList):
	if direction == 'right':
		head = pygame.transform.rotate(img, 270)
	elif direction == 'left':
		head = pygame.transform.rotate(img, 90)
	elif direction == 'up':
		head = img
	elif direction == 'down':
		head = pygame.transform.rotate(img, 180)


	# gameDisplay.blit(img, (snackList[-1][0], snackList[-1][1]))
	gameDisplay.blit(head, (snackList[-1][0], snackList[-1][1]))
	for XnY in snackList[:-1]:
		#pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, block_size, block_size])
		pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])
'''
def randAppleGen(): # random apple position generator
	randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10.0 
	randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10.0
	return randAppleX, randAppleY
'''
def score(score): # add the score to the top left of the screen
	text = smallfont.render("Score: " + str(score), True, black)
	gameDisplay.blit(text, [0, 0])
'''
def pause():
	pause = True
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				#quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					#quit()
					sys.exit()
				elif event.key == pygame.K_c:
					pause = False

		gameDisplay.fill(white)
		message_to_screen("Paused", black, -100, size = "large")
		message_to_screen("Press C to continue, Q to quit", black, 25)
		pygame.display.update()
		clock.tick(5) # cannot pause forever
'''
# Another way to pause the game:
def pause():
	pause = True

	message_to_screen("Paused", black, -100, size = "large")
	message_to_screen("Press C to continue, Q to quit", black, 25)
	pygame.display.update()
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				#quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					#quit()
					sys.exit()
				elif event.key == pygame.K_c:
					pause = False

# create start menu:
def game_intro():

	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				#quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					#quit()
					sys.exit()
				elif event.key == pygame.K_c:
					intro = False

		gameDisplay.fill(white)
		message_to_screen("Welcome to Slither", green, -100, "large")
		message_to_screen("The objects of the game is to eat red apples", black, -30)
		message_to_screen("The more apples you eat, the longer you get", black, 10)
		message_to_screen("If you run into yourself, or the edges, you die!", black, 50)
		message_to_screen("Press C to play or Q to quit or P to pause", black, 180)

		pygame.display.update()
		clock.tick(10)


# create a loop for the game:
def gameLoop():
	global direction # with global, we can modify variables; without globol we can only reference it
	# these variables below are about to change for each loop
	gameExit = False
	gameOver = False

	lead_x = display_width/2 # location of head of snack
	lead_y = display_height/2
	lead_x_change = 20 # changing variable for changing x; default is going right at begining
	lead_y_change = 0

	snackList = []
	snackLength = 1 # maxmum length of snack that is allowed for the snack

	global AppleThickness
	#AppleThickness = random.randint(5, 30) # to increate the size of Apples
	AppleThickness = 20

	randAppleX = round(random.randrange(0, display_width - AppleThickness)/10.0) * 10.0 # create random position of apple; and make it always the multiple of 10 to align with snake.
	randAppleY = round(random.randrange(0, display_height - AppleThickness)/10.0) * 10.0

	while not gameExit:
		if gameOver == True: # this is to keep score and other objects when game is over!
			message_to_screen("Game Over", red, y_displace = -50, size = "large")
			message_to_screen("Press C to continue or Q to quit!", black, y_displace = 50, size = "medium")
			pygame.display.update()
		while gameOver == True:
			#gameDisplay.fill(white)
			message_to_screen("Game Over", red, y_displace = -50, size = "large")
			message_to_screen("Press C to continue or Q to quit!", black, y_displace = 50, size = "medium")
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					elif event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			#print(event) # print the event when doing anything on the window
			# for all events: www.pygame.org/docs/ref/event.html
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and lead_x_change != block_size: # hit left arrow
					direction = 'left'
					#lead_x -= 10
					lead_y_change = 0 # this is to stop changing y when user start to change x
					lead_x_change = -block_size
				elif event.key == pygame.K_RIGHT and lead_x_change != -block_size: # hit right arrow
					direction = 'right'
					#lead_x += 10
					lead_y_change = 0
					lead_x_change = block_size
				elif event.key == pygame.K_UP and lead_y_change != block_size: # lead_x_change != 10 is just to avoid snack to coming reversely
					direction = 'up'
					lead_x_change = 0
					lead_y_change = -block_size
				elif event.key == pygame.K_DOWN and lead_y_change != -block_size: 
					direction = 'down'
					lead_x_change = 0
					lead_y_change = block_size
				elif event.key == pygame.K_p:
					pause()
			'''
			# when user release the key, reset the lead_x_change variable to 0! But this is not part of snack game!
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
			'''
		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0: # set boundaries for snack
			#gameExit = True
			gameOver = True

		lead_x += lead_x_change
		lead_y += lead_y_change

		gameDisplay.fill(white) # set the background to white
		#pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness]) # creating an apple
		gameDisplay.blit(appleimg, (randAppleX, randAppleY))
		
		snackHead = []
		snackHead.append(lead_x)
		snackHead.append(lead_y)
		snackList.append(snackHead)

		if len(snackList) > snackLength: # the length of snack cannot exceed the max setted
			del snackList[0]

		for eachSegment in snackList[:-1]: # this is the collision function when snack head again show in the list
			if eachSegment == snackHead:
				gameOver = True

		snack(block_size, snackList)			
		# pygame.draw.rect(gameDisplay, black, [400, 300, 10, 100]) # start x, y, width, height
		# pygame.draw.rect(gameDisplay, red, [400, 300, 10, 10]) this will be uplayer
		# gameDisplay.fill(red, rect = [200, 200, 50, 50]) # another way to draw rect
		score(snackLength - 1)
		pygame.display.update() # this is to update the display to make motions
	# this is the same as pygram.display.flip()

		#if lead_x == randAppleX and lead_y == randAppleY: # eating an apple
		'''
		if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness - 10:
			if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness - 10:
				randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10.0 
				randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10.0
				snackLength += 1
		'''
		# Cases become more complex when size of apple and snack become random:
		if ((lead_x >= randAppleX and lead_x < randAppleX + AppleThickness) or (lead_x + block_size > randAppleX and lead_x + block_size <= randAppleX + AppleThickness)) or ((lead_x <= randAppleX and lead_x + block_size > randAppleX) or (lead_x < randAppleX + AppleThickness and lead_x + block_size >= randAppleX + AppleThickness)):
			if ((lead_y >= randAppleY and lead_y < randAppleY + AppleThickness) or (lead_y + block_size > randAppleY and lead_y + block_size <= randAppleY + AppleThickness)) or ((lead_y <= randAppleY and lead_y + block_size > randAppleY) or (lead_y < randAppleY + AppleThickness and lead_y + block_size >= randAppleY + AppleThickness)):
				randAppleX = round(random.randrange(0, display_width - AppleThickness)/10.0) * 10.0 
				randAppleY = round(random.randrange(0, display_height - AppleThickness)/10.0) * 10.0
				snackLength += 1
				#AppleThickness = random.randint(5, 30) # to increate the size of Apples

		clock.tick(FPS) # 15 Fps, this is to control the speed of the game

	#message_to_screen("You Lose!", red)
	pygame.display.update() # if we want some object to update graphics OR text on the screen
	time.sleep(2)
	pygame.quit() # this is to end the game

	#quit() # this is to close the window
	sys.exit()
if __name__ == "__main__":
	game_intro()
	gameLoop()