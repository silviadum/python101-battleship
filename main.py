import os
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Battleships")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

font = pygame.font.Font('font/pixelated.ttf', 30)
running = 1


# start menu
def start_menu():
    font = pygame.font.Font('font/pixelated.ttf', 40)
    start = font.render("     PRESS S FOR START", True, (255, 255, 255))
    font2 = pygame.font.Font('font/pixelated.ttf', 70)
    title = font2.render("      BATTLESHIPS", True, (74, 198, 183))
    screen.fill((0, 0, 50))
    screen.blit(start, (330, 570))
    screen.blit(title, (220, 320))
    vector_image = load_images('images')
    battle_ship = pygame.transform.scale(vector_image[0], (700, 500))
    screen.blit(battle_ship, (240, -50))
    pygame.display.update()

# load image
def load_images(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name)
        images.append(image)
    return images


# main function
while running:
    # default customization start menu
    start_menu()

