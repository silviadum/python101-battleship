import pygame

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#create display window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
clock = pygame.time.Clock()
fps=60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battleship')
bg_image = pygame.image.load('BIGwarship.jpg ')
#load button images
start_img = pygame.image.load('start.png')
exit_img = pygame.image.load('whiteflag1.png')

#create button instances
start_button = Button(500, 200, start_img, 0.1)
exit_button = Button(500, 400, exit_img, 0.2)

#game loop
run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw():
        print('START')
        screen.fill((202, 228, 241))
        
    if exit_button.draw():
        print('EXIT')
        run =False

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
    
    #fps
    clock.tick(fps)
    pygame.display.update()

pygame.quit()