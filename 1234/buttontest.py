import pygame
import sys

pygame.init()
transparent = (0,0,0,0)
xmax=800
ymax=800
menu=0

screen = pygame.display.set_mode((xmax,ymax))
pygame.display.set_caption("O iubesc pe iubi bubi")
main_font = pygame.font.SysFont("cambria",20)
#fps cap
clock = pygame.time.Clock()
fps=60
#buton
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
            
    def checkForInput(self,position,numar):
        
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("s a apasat")
            
                
    def hover(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "red")
        else:
            self.text = main_font.render(self.text_input, True, "black")
#facem butonul de start
button_surface=pygame.image.load("start.png")
button_surface=pygame.transform.scale(button_surface, (150,150))
buttonstart= Button(button_surface, 400, 400, "START")
img1=buttonstart.image

#facem buton de quit
buttonquit_surface=pygame.image.load("whiteflag1.png")
buttonquit_surface=pygame.transform.scale(buttonquit_surface, (150,150))
buttonquit=Button(buttonquit_surface,400,600,"QUIT") 
#background
game_display = pygame.display.set_mode((xmax, ymax))
# Loading the image
bg_image = pygame.image.load('BIGwarship.jpg ')
#warship?
#warship=pygame.image.load('warship.webp')
#menu=1
loser=False

#incepe jocul
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #verifica daca butonul e apasat
            #buttonstart.update()
            buttonstart.checkForInput(pygame.mouse.get_pos())
            #buttonstart.ButonStart(pygame.mouse.get_pos())
            #game_display.blit(bg_image, (0, 0))
            
    
    #pt background
    game_display.blit(bg_image, (0, 0))
    #pt buton
    
    buttonstart.update()
    buttonstart.hover(pygame.mouse.get_pos())
    #buttonstart.ButonStart(pygame.mouse.get_pos())
    buttonquit.update()
    buttonquit.hover(pygame.mouse.get_pos())
    #game_display.blit(warship,(300,200))
    #idk sincer
    pygame.display.update()
    #fps
    clock.tick(fps)