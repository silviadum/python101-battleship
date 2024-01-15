import pygame

# initializing the constructor 
pygame.init() 

# screen resolution 
# opens up a window 
window = pygame.display.set_mode((800, 600))
red_button = pygame.Surface((50, 50)) 
red_button.fill("pink")
window.blit(red_button, (200, 200)) 
pygame.display.update()

while True:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if red_button.get_rect().collidepoint(pos):
				red_button.fill("red")
				print("1234")



