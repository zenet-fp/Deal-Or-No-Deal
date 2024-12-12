import random



class NoughtsCrosses:
    def __init__(self):
        self.score = []
        self.user_decide = False
        self.ai_decide = False
        self.player_piece = None
        self.ai_piece = None
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.positions = {"TL" : [0, 0], "TM" : [0, 1],
                     "TR" : [0, 2], "ML" : [1, 0],
                     "MM" : [1, 1], "MR" : [1, 2],
                     "BL" : [2, 0], "BM" : [2, 1],
                     "BR" : [2, 2]
        }



    def main_game(self):

        winner = DecideWinner()
        while self.user_decide is False and self.ai_decide is False:

            self.user_choice()
            winner.choose_winner()
            if self.user_decide is True or self.ai_decide is True:

                break

            self.ai_choice()
            winner.choose_winner()
            if self.user_decide is True or self.ai_decide is True :

                break

            self.game_board()


    def game_board(self):
        for row in self.board:
            print("|", end=" ")
            for cell in row:
                print(cell, end=" | ")
            print("\n-------------")

    print()

    def user_choice(self):

        print()
        print(f"These are your positions: {list(self.positions.keys())}")
        print("<-------------------------------------------------------------------------------->")

        while self.player_piece is None:
            self.game_board()

            user_piece = str((input("Which piece are you using: Noughts or Crosses? (O / X) : "))).upper()
            self.player_piece = user_piece
            break


        l = True
        while l:

     

            user_position = input("Which position would you like to place your piece?: ").upper()
            print("<-------------------------------------------------------------------------------->")
            print()
            if user_position in self.positions:

                val, val2 = self.positions[user_position]

                if self.board[val][val2] == " ":

                    self.board[val][val2] = f"{self.player_piece}"
                    self.positions.pop(user_position)

                    break

                else:
                    print("A piece is already in that position.")

            else:
                print("An error occurred")
                self.user_choice()

    
    def ai_choice(self):

        ai_row = random.randint(0, 2)
        ai_column = random.randint(0, 2)
        ai_piece = "X" if self.player_piece == "O" else "O"

        if self.board[ai_row][ai_column] != " ":
            self.ai_choice()

        else:
            self.ai_piece = ai_piece
            self.board[ai_row][ai_column] = f"{ai_piece}"



class DecideWinner(NoughtsCrosses):
    def __init__(self):
        super().__init__()

    def choose_winner(self):
            x = self.player_piece
            for i in range(3):

                if self.board[0][i] ==  self.board[1][i] == self.board[2][i] != " ":

                    if self.board[0][i] == x:
                        self.user_decide =  True
                        self.game_board()
                        print(f"The player has won three in a row!")

                    else:
                        self.ai_decide = True
                        self.game_board()
                        print(f"The AI has beaten the player! ")

            if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":

                if self.board[0][0] == x:
                    self.user_decide = True
                    self.game_board()
                    print(f"The player has won three in a row!")

                else:
                    self.ai_decide = True
                    self.game_board()
                    print(f"The AI has beaten the player! ")

            if self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":

                if self.board[2][0] == x:
                    self.user_decide = True
                    self.game_board()
                    print(f"The player has won three in a row!")

                else:
                    self.ai_decide = True
                    self.game_board()
                    print(f"The AI has beaten the player! ")


if __name__ == '__main__':
    x_ = NoughtsCrosses()
    x_.main_game()










