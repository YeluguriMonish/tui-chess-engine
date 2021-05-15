import chess
import chess.engine
from blessed import Terminal

term = Terminal()
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
engine = chess.engine.SimpleEngine.popen_uci(
    "./Stockfish-master/src/stockfish")
engine.close()

with term.cbreak(), term.hidden_cursor(), term.fullscreen():
    move = ""
    while True:
        print(term.home + term.clear)
        print(board)
        print("enter move: " + move)
        inp = term.inkey()
        if inp.isdigit() or inp.isalpha():
            move = move + inp
        if inp.code == 263:
            move = move[:-1]
        if inp == 'q':
            break
        if inp.code == 343:
            try:
                x = chess.Move.from_uci(move)
                if x in board.legal_moves:
                    board.push(x)
            except ValueError:
                pass
            move = ""
