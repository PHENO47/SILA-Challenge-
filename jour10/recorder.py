"""
recorder.py
-----------

Enregistrement des parties en notation algébrique.
Exemple :
1. X A1
2. O B2
"""

from typing import List


class Recorder:

    def __init__(self) -> None:
        self.moves: List[str] = []

    def to_algebraic(self, row: int, col: int) -> str:
        letter = chr(ord("A") + col)
        return f"{letter}{row + 1}"

    def record(self, player: str, row: int, col: int) -> None:
        move_notation = f"{player} {self.to_algebraic(row, col)}"
        self.moves.append(move_notation)

    def save(self, filename: str = "game.txt") -> None:
        with open(filename, "w") as f:
            for i, move in enumerate(self.moves):
                f.write(f"{i + 1}. {move}\n")