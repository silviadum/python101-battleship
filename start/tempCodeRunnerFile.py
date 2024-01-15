button_rect = pygame.Rect(0, 0, 100, 50)

# Create a pygame.event.MOUSEBUTTONDOWN event handler that checks if the mouse is clicked inside the button's boundaries
def on_mouse_button_down(event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_rect.collidepoint(event.pos):
        print("Button clicked!")

pygame.display.update()