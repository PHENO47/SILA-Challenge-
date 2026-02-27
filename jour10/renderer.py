"""
renderer.py
-----------

Responsable uniquement de l'affichage Pygame.
Séparation stricte logique / rendu (important en compétition).
"""

import pygame
from config import *


class Renderer:

    def __init__(self, screen, board):
        self.screen = screen
        self.board = board

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self._draw_grid()
        self._draw_symbols()

    def _draw_grid(self):
        size = self.board.size
        cell = WINDOW_SIZE // size

        for i in range(1, size):
            pygame.draw.line(
                self.screen, GRID_COLOR,
                (0, i * cell),
                (WINDOW_SIZE, i * cell), 2
            )
            pygame.draw.line(
                self.screen, GRID_COLOR,
                (i * cell, 0),
                (i * cell, WINDOW_SIZE), 2
            )

    def _draw_symbols(self):
        size = self.board.size
        cell = WINDOW_SIZE // size

        for r in range(size):
            for c in range(size):
                value = self.board.grid[r][c]
                center = (
                    c * cell + cell // 2,
                    r * cell + cell // 2
                )

                if value == "X":
                    offset = cell // 3
                    pygame.draw.line(self.screen, X_COLOR,
                                     (center[0] - offset, center[1] - offset),
                                     (center[0] + offset, center[1] + offset), 3)
                    pygame.draw.line(self.screen, X_COLOR,
                                     (center[0] - offset, center[1] + offset),
                                     (center[0] + offset, center[1] - offset), 3)

                elif value == "O":
                    pygame.draw.circle(self.screen, O_COLOR,
                                       center, cell // 3, 3)