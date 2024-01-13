import os
import random
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Battleships")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

font = pygame.font.Font('font/pixelated.ttf', 30)
running = 1


# bot function for hitting
def bot(matrix):
    while 1:
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        if matrix[i][j] == 0:
            matrix[i][j] = -1
            return 0

        if matrix[i][j] == 1:
            matrix[i][j] = -2
            return 1

        if matrix[i][j] == 2:
            matrix[i][j] = -2
            return 2

        if matrix[i][j] == 3:
            matrix[i][j] = -2
            return 3


# verify
def show_ship(see_ship1, see_ship2, see_ship3, ship_remain, ship_remain_bot):
    # global variables
    global running

    # check to display boat
    if see_ship1 == 1:
        screen.blit(ship1, (ship1_x, ship1_y - 5))
    if see_ship2 == 1:
        screen.blit(ship2, (ship2_x - 7, ship2_y - 12))
    if see_ship3 == 1:
        screen.blit(ship3, (ship3_x + 5, ship3_y))

    # check for ending game
    if ship_remain == 0 or ship_remain_bot == 0:
        # game result
        if ship_remain == 0:
            winner = font.render("YOU WIN!!!", True, (121, 188, 184))
        else:
            winner = font.render("COMPUTER WINS!!!", True, (121, 188, 184))
        # display winner
        screen.blit(winner, (550, 675))
        pygame.display.update()


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

    # catch an event
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = 0
        # press start => function game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                game()