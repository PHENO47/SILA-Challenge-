"""
ai.py
-----

Implémentation d'une IA basée sur Minimax avec élagage Alpha-Bêta.
Inclut 3 niveaux de difficulté.
"""

import math
import random
from typing import Tuple, Optional
from board import Board


class AI:
    """Intelligence artificielle du jeu."""

    def __init__(self, level: str = "impossible") -> None:
        self.level = level

    def choose_move(
        self,
        board: Board,
        ai_player: str,
        human_player: str
    ) -> Tuple[int, int]:
        """
        Sélectionne le meilleur coup selon le niveau.
        """

        # Niveau facile → aléatoire
        if self.level == "easy":
            return random.choice(board.empty_cells())

        depth_limit: Optional[int] = None

        # Niveau moyen → profondeur limitée
        if self.level == "medium":
            depth_limit = 3

        best_score = -math.inf
        best_move = None

        # Tri des coups (centre prioritaire)
        moves = board.empty_cells()
        moves.sort(key=lambda move: self._move_priority(move, board.size))

        for (row, col) in moves:
            board.play(row, col, ai_player)
            score = self._minimax(
                board,
                False,
                ai_player,
                human_player,
                -math.inf,
                math.inf,
                depth_limit,
                0
            )
            board.undo(row, col)

            if score > best_score:
                best_score = score
                best_move = (row, col)

        return best_move

    def _move_priority(self, move, size: int) -> int:
        """
        Priorise les cases centrales pour améliorer l'élagage.
        """
        center = size // 2
        return abs(move[0] - center) + abs(move[1] - center)

    def _minimax(
        self,
        board: Board,
        maximizing: bool,
        ai_player: str,
        human_player: str,
        alpha: float,
        beta: float,
        depth_limit: Optional[int],
        depth: int
    ) -> int:

        # États terminaux
        if board.check_winner(ai_player):
            return 100 - depth
        if board.check_winner(human_player):
            return depth - 100
        if board.is_full():
            return 0

        if depth_limit is not None and depth >= depth_limit:
            return 0

        if maximizing:
            max_eval = -math.inf
            for (r, c) in board.empty_cells():
                board.play(r, c, ai_player)
                eval_score = self._minimax(
                    board, False,
                    ai_player, human_player,
                    alpha, beta,
                    depth_limit,
                    depth + 1
                )
                board.undo(r, c)

                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Alpha-Bêta pruning
            return max_eval

        else:
            min_eval = math.inf
            for (r, c) in board.empty_cells():
                board.play(r, c, human_player)
                eval_score = self._minimax(
                    board, True,
                    ai_player, human_player,
                    alpha, beta,
                    depth_limit,
                    depth + 1
                )
                board.undo(r, c)

                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval