import pygame,random,sys


#################################
# Variables
screen_width = 800
screen_hight = 600
fps = 60
clock = pygame.time.Clock()
window_name = "P2Crawler"

#################################

#initiate the game
pygame.init()

#initiate the window
screen = pygame.display.set_mode((screen_width,screen_hight))

#set the title
pygame.display.set_caption(window_name)

#set the background color
screen.fill((0,0,0))

#