from cols import *

class chess:
    def __init__(self, colour):
        self.colour = colour
        self.board = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
                      ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                      ['wr', 'wn', 'ww', 'wq', 'wk', 'ww', 'wn', 'wr']]


    def print_board(self):
        for j in range(8):
            for i in range(8):
                print(f"{bg_light_green if (i+j) % 2 == 0 else bg_green}      {bg_reset}", end="")
            print()
            for i in range(8):
                if self.board[j][i] is None:
                    print(f"{bg_light_green if (i+j) % 2 == 0 else bg_green}      {bg_reset}", end="")
                    continue
                bg_col = bg_light_green if (i+j) % 2 == 0 else bg_green 
                fg_col = text_black if self.board[j][i][0] == 'b' else text_white
                print(f"{bg_col}{fg_col}{text_bold}   {self.board[j][i][1].upper()}  {text_reset}{bg_reset}", end="")
            print()
            for i in range(8):
                print(f"{bg_light_green if (i+j) % 2 == 0 else bg_green}      {bg_reset}", end="")
            print()



if __name__ == "__main__":
    c = chess("white")
    c.print_board()
