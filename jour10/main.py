"""
main.py
-------

Point d'entrée principal du programme.
Gère la boucle principale Pygame.
"""

import pygame
from game import Game
from config import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Morpion IA - Minimax Alpha-Beta")

    clock = pygame.time.Clock()

    game = Game(screen)

    while game.running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(pygame.mouse.get_pos())

        game.update()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()