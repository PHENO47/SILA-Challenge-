"""
board.py
--------

Gestion du plateau de jeu N×N.
Responsabilités :
- Stockage de la grille
- Validation des coups
- Détection de victoire
- Annulation de coups (nécessaire pour Minimax)
"""

from typing import List, Tuple, Optional


class Board:
    """Représente un plateau de morpion extensible."""

    def __init__(self, size: int = 3) -> None:
        self.size: int = size
        self.grid: List[List[str]] = [
            ["" for _ in range(size)] for _ in range(size)
        ]

    def play(self, row: int, col: int, player: str) -> bool:
        """
        Place un symbole sur le plateau.
        Retourne True si le coup est valide.
        """
        if self.grid[row][col] == "":
            self.grid[row][col] = player
            return True
        return False

    def undo(self, row: int, col: int) -> None:
        """Annule un coup (utilisé par Minimax)."""
        self.grid[row][col] = ""

    def empty_cells(self) -> List[Tuple[int, int]]:
        """Retourne toutes les cases vides."""
        return [
            (r, c)
            for r in range(self.size)
            for c in range(self.size)
            if self.grid[r][c] == ""
        ]

    def is_full(self) -> bool:
        """Vérifie si la grille est pleine."""
        return all(cell != "" for row in self.grid for cell in row)

    def check_winner(self, player: str) -> bool:
        """Vérifie si un joueur a gagné."""

        size = self.size

        # Vérification lignes
        for row in self.grid:
            if all(cell == player for cell in row):
                return True

        # Vérification colonnes
        for col in range(size):
            if all(self.grid[row][col] == player for row in range(size)):
                return True

        # Diagonales principales
        if all(self.grid[i][i] == player for i in range(size)):
            return True

        if all(self.grid[i][size - i - 1] == player for i in range(size)):
            return True

        return False