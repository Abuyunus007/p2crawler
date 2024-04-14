import pygame,random,sys

pygame.init()
pygame.font.init()

#################################
# Variables
screen_width = 800
screen_hight = 600
fps = 60
clock = pygame.time.Clock()
window_name = "P2Crawler"
font = pygame.font.SysFont("ArialBold",72)
Text_color = (255,255,255)
#################################

screen = pygame.display.set_mode((screen_width,screen_hight))

#set the title
pygame.display.set_caption(window_name)

#set the background color
screen.fill((52,70,91))

def draw_text(text,font, Text_color,x,y):  
    text_surface = font.render(text,True,Text_color)
    screen.blit(text_surface,((screen_width/2)-text_surface.get_width()/2,(screen_hight/2)-text_surface.get_height()/2))

#################################
# Game Loop
run = True

while run:
    draw_text("Press SPACE to Continue", font, Text_color, 150, 250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
sys.exit()
#################################
# Functions