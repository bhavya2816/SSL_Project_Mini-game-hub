import numpy as np
from games.base_game import BaseGame


class TicTacToe(BaseGame):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)

        # 10x10 board (0 = empty, 1 = player1, -1 = player2)
        self.board = np.zeros((10, 10), dtype=int)

        # Map players to values
        self.player_map = {
            self.player1: 1,
            self.player2: -1
        }

    # =========================
    # MAKE MOVE
    # =========================
    def make_move(self, row, col):
        if self.board[row, col] != 0:
            return False  # invalid move

        self.board[row, col] = self.player_map[self.current_player]
        self.switch_turn()
        return True

    # =========================
    # CHECK WINNER (NO LOOPS)
    # =========================
    def check_winner(self):
        board = self.board

        # Helper: check if any 5 consecutive values sum to ±5
        def check_lines(arr):
            # Sliding window sum using convolution
            kernel = np.ones(5, dtype=int)
            conv = np.apply_along_axis(
                lambda x: np.convolve(x, kernel, mode='valid'),
                axis=1,
                arr=arr
            )
            return np.any(conv == 5) or np.any(conv == -5)

        # Horizontal
        if check_lines(board):
            return self.get_winner_name()

        # Vertical
        if check_lines(board.T):
            return self.get_winner_name()

        # Diagonals (main + flipped)
        diagonals = np.array([board.diagonal(i) for i in range(-5, 6)], dtype=object)
        anti_diagonals = np.array([np.fliplr(board).diagonal(i) for i in range(-5, 6)], dtype=object)

        for diag_group in [diagonals, anti_diagonals]:
            for diag in diag_group:
                if len(diag) >= 5:
                    conv = np.convolve(diag, np.ones(5), mode='valid')
                    if np.any(conv == 5) or np.any(conv == -5):
                        return self.get_winner_name()

        return None

    # =========================
    # HELPER
    # =========================
    def get_winner_name(self):
        # Since turn already switched after move,
        # winner is the previous player
        return (
            self.player2 if self.current_player == self.player1
            else self.player1
        )
