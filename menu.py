import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Welcome to the game")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BTN_HOVER = (50, 70, 90)
# font déclaration
FONT = pygame.font.SysFont ("Times New Norman", 60)
# Buttons déclaration


text1 = FONT.render("START", True, WHITE)
text2 = FONT.render("SETTINGS", True, WHITE)
text3 = FONT.render("Quit", True, WHITE)

rect1 = pygame.Rect(300, 300, 205, 80)
rect2 = pygame.Rect(300, 400, 205, 80)
rect3 = pygame.Rect(300, 500, 205, 80)

buttons = [
    [text1, rect1, BLACK],
    [text2, rect2, BLACK],
    [text3, rect3, BLACK]
]



def jeu_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    if button[1].collidepoint(event.pos):
                    #set the button color to BTN_HOVER color
                        button[2] = BTN_HOVER
                    else:
                        # other<wise reset the color to black
                        button[2] = BLACK

        screen.fill((20, 50, 70))

        #Dessiner les buttons avec les couleurs
        for text, rect, color in buttons:
            text_rect = text.get_rect(center=(800/2, 600/2))
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect,)

        pygame.display.flip()
        clock.tick(15)

jeu_intro()
pygame.quit()
