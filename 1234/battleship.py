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
main_font=pygame.font.SysFont(None,72)
pygame.display.set_caption("O iubesc pe iubi bubi")
class Button():
    def __init__(self,image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.rect= self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text=main_font.render(self.text_input,True,"white")
        self.text_rect=self.text.get_rect(center=(self.x_pos,self.y_pos))
        
    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
            
    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("s a apasat")
            
                
    def hover(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "black")
        else:
            self.text = main_font.render(self.text_input, True, "white")
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

button_surface=pygame.image.load("butonpula.png")
button = Button(button_surface, 300, 300, "Click me!")
running = True
background = ts
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())
    button.update()
    button.hover(pygame.mouse.get_pos())
            
    screen.fill(background)
    screen.blit(img, (610, 450))
    screen.blit(img1, (610, 250))
    screen.blit(img2, (550, 350))
    pygame.display.update()

pygame.quit()