import tkinter as tk
from tkinter import simpledialog, messagebox

class TicTacToeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")

        self.players = self.get_players()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 0

        self.create_widgets()

    def get_players(self):
        player_x = simpledialog.askstring("Player X", "Enter name for Player X:")
        player_o = simpledialog.askstring("Player O", "Enter name for Player O:")
        return [player_x, player_o]

    def create_widgets(self):
        self.label_turn = tk.Label(self, text=f"Turn: {self.players[self.current_player]}", font=("Helvetica", 12))
        self.label_turn.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self, text="", width=5, height=2,
                                              command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i + 1, column=j, padx=5, pady=5)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=4, column=1, pady=10)

    def on_button_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = "X" if self.current_player == 0 else "O"
            if self.check_win():
                messagebox.showinfo("Game Over", f"{self.players[self.current_player]} wins!")
                self.reset_game()
            elif all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 1 - self.current_player
                self.label_turn.config(text=f"Turn: {self.players[self.current_player]}")

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = 0
        self.label_turn.config(text=f"Turn: {self.players[self.current_player]}")

    def check_win(self):
        for row in self.buttons:
            if row[0]["text"] == row[1]["text"] == row[2]["text"] and row[0]["text"] != "":
                return True
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] and self.buttons[0][col]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] and self.buttons[0][0]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] and self.buttons[0][2]["text"] != "":
            return True
        return False

if __name__ == "__main__":
    game = TicTacToeGame()
    game.mainloop()
