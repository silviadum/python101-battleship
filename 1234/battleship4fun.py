"""Draw text to the screen."""
import pygame
from pygame.locals import *
import time
ts= (189,231,249)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
pygame.init()
screen = pygame.display.set_mode((1360, 760))
sysfont = pygame.font.get_default_font()
font = pygame.font.Font(None, 72)

img = font.render("QUIT", True, "black", "red")
rect = img.get_rect()
pygame.draw.rect(img, "black", rect, 1)

##font1 = pygame.font.SysFont('chalkduster.ttf', 72, bold= False, italic= False)
img1 = font.render('PLAY', True, "black", "red")
rect1=img1.get_rect()
pygame.draw.rect(img1, "black", rect1, 1)

##font2 = pygame.font.SysFont('didot.ttc', 72)
img2 = font.render('SETTINGS', True, "black","red")
rect2=img2.get_rect()
pygame.draw.rect(img2, "black", rect2, 1)





running = True
background = ts
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(background)
    screen.blit(img, (610, 450))
    screen.blit(img1, (610, 250))
    screen.blit(img2, (550, 350))
    pygame.display.update()

pygame.quit()