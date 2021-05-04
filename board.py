import chess
from blessed import Terminal

term = Terminal()
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

with term.cbreak(), term.hidden_cursor():
    exit = False
    inputting = True
    move = ""
    while inputting:
        print(term.home + term.clear)
        print(board)
        print("enter move: " + move)
        inp = term.inkey()
        if inp.code != 343:
            move = move + inp
        if inp.code == 343:
            x = chess.Move.from_uci(move)
            board.push(x)
            move = ""
