"""
game.py
-------

Gestion complète du jeu :
- Score conservé entre les parties
- IA intégrée
- Boutons Rejouer / Quitter
- Overlay de fin
- Sécurisé contre erreurs NoneType
"""

import pygame
from board import Board
from ai import AI
from recorder import Recorder
from renderer import Renderer
from config import *


class Game:

    def __init__(self, screen, size=DEFAULT_BOARD_SIZE,
                 ai_level=DEFAULT_AI_LEVEL,
                 mode="ai"):

        self.screen = screen
        self.size = size
        self.ai_level = ai_level
        self.mode = mode

        # Score global (persistant durant la session)
        self.score = {"X": 0, "O": 0}

        self.running = True
        self._init_new_game()

    # -------------------------------------------------
    # Initialisation d'une nouvelle partie
    # -------------------------------------------------
    def _init_new_game(self):
        self.board = Board(self.size)
        self.ai = AI(self.ai_level)
        self.recorder = Recorder()
        self.renderer = Renderer(self.screen, self.board)

        self.current_player = "X"
        self.game_over = False
        self.winner_message = ""

        self.replay_button = None
        self.quit_button = None

    # -------------------------------------------------
    # Gestion des clics souris
    # -------------------------------------------------
    def handle_click(self, pos):

        # Si partie terminée → gestion boutons
        if self.game_over:
            self._handle_buttons(pos)
            return

        cell = WINDOW_SIZE // self.board.size
        col = pos[0] // cell
        row = pos[1] // cell

        # Vérifie que le clic est dans la grille
        if row >= self.board.size or col >= self.board.size:
            return

        if self.board.play(row, col, self.current_player):
            self.recorder.record(self.current_player, row, col)

            if not self._check_game_over():
                self._switch_player()
                self._ai_move_if_needed()

    # -------------------------------------------------
    # IA
    # -------------------------------------------------
    def _ai_move_if_needed(self):
        if self.mode == "ai" and self.current_player == "O":

            pygame.time.delay(300)  # petite pause effet réflexion

            row, col = self.ai.choose_move(self.board, "O", "X")
            self.board.play(row, col, "O")
            self.recorder.record("O", row, col)

            if not self._check_game_over():
                self._switch_player()

    # -------------------------------------------------
    def _switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    # -------------------------------------------------
    # Vérifie fin de partie
    # -------------------------------------------------
    def _check_game_over(self):

        if self.board.check_winner(self.current_player):
            self.score[self.current_player] += 1
            self.winner_message = f"🎉 {self.current_player} gagne !"
            self._end_game()
            return True

        if self.board.is_full():
            self.winner_message = "🤝 Match nul !"
            self._end_game()
            return True

        return False

    # -------------------------------------------------
    # Fin de partie
    # -------------------------------------------------
    def _end_game(self):
        self.game_over = True
        self.recorder.save()

        # Création boutons
        self.replay_button = pygame.Rect(
            WINDOW_SIZE // 4,
            WINDOW_SIZE - 80,
            150, 50
        )

        self.quit_button = pygame.Rect(
            WINDOW_SIZE // 2,
            WINDOW_SIZE - 80,
            150, 50
        )

    # -------------------------------------------------
    # Gestion clic boutons
    # -------------------------------------------------
    def _handle_buttons(self, pos):

        # Sécurité anti-erreur NoneType
        if self.replay_button and self.replay_button.collidepoint(pos):
            self._init_new_game()
            return

        if self.quit_button and self.quit_button.collidepoint(pos):
            self.running = False

    # -------------------------------------------------
    # Dessin principal appelé par main.py
    # -------------------------------------------------
    def update(self):
        self.renderer.draw()
        self._draw_score()

        if self.game_over:
            self._draw_overlay()

    # -------------------------------------------------
    # Affichage score
    # -------------------------------------------------
    def _draw_score(self):

        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render(
            f"Score  X : {self.score['X']}  |  O : {self.score['O']}",
            True,
            (255, 255, 255)
        )

        self.screen.blit(text, (10, 10))

    # -------------------------------------------------
    # Overlay de fin + boutons
    # -------------------------------------------------
    def _draw_overlay(self):

        overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Message victoire
        font = pygame.font.SysFont("arial", 48, bold=True)
        text = font.render(self.winner_message, True, (255, 255, 255))
        rect = text.get_rect(center=(WINDOW_SIZE // 2,
                                     WINDOW_SIZE // 2 - 40))
        self.screen.blit(text, rect)

        # Bouton Rejouer
        pygame.draw.rect(self.screen, (46, 204, 113),
                         self.replay_button, border_radius=10)
        replay_text = pygame.font.SysFont("arial", 24).render(
            "Rejouer", True, (0, 0, 0)
        )
        self.screen.blit(
            replay_text,
            replay_text.get_rect(center=self.replay_button.center)
        )

        # Bouton Quitter
        pygame.draw.rect(self.screen, (231, 76, 60),
                         self.quit_button, border_radius=10)
        quit_text = pygame.font.SysFont("arial", 24).render(
            "Quitter", True, (0, 0, 0)
        )
        self.screen.blit(
            quit_text,
            quit_text.get_rect(center=self.quit_button.center)
        )