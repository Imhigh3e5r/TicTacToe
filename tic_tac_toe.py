import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" "] * 9
        self.buttons = []

        self.create_board()
        self.window.mainloop()

    def create_board(self):
        """Creates a 3x3 grid of buttons for the game."""
        for i in range(9):
            btn = tk.Button(self.window, text=" ", font=("Arial", 20), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def make_move(self, position):
        """Handles a player's move when a button is clicked."""
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Checks if a player has won the game."""
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != " ":
                return self.board[a]  # Return winner ("X" or "O")
        return None

    def check_draw(self):
        """Checks if the game is a draw."""
        return " " not in self.board

    def reset_game(self):
        """Resets the game board."""
        self.board = [" "] * 9
        for btn in self.buttons:
            btn.config(text=" ")
        self.current_player = "X"

# Run the game
TicTacToe()
