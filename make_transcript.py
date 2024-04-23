import chess.pgn
import sys
from pathlib import Path

def pgn_move_to_human_text(move):
    move_str = ""
    if move == "O-O":
        return "King side castle [[slnc 3000]]"
    elif move == "O-O-O":
        return "Queen side castle [[slnc 3000]]"

    notation_to_english_map = {
        "a": "[[char LTRL]] a [[char NORM]]",
        "x": " takes ",
        "+": " with check ",
        "#": " with checkmate.",
        "=": " promotes to ",
        "K": "King ",
        "Q": "Queen ",
        "R": "Rook ",
        "N": "Knight ",
        "B": "Bishop ",
        "1": "one ",
        "2": "two ",
        "3": "three ",
        "4": "four ",
        "5": "five ",
        "6": "six ",
        "7": "seven ",
        "8": "eight ",
    }

    for chr in move:
        if chr in notation_to_english_map:
            move_str += notation_to_english_map[chr]
        else:
            move_str += chr + " "

    return move_str + " [[slnc 3000]] "

def result_to_human_text(outcome):
    if outcome == "1-0":
        return "White wins"
    elif outcome == "0-1":
        return "Black wins"
    else:
        return "Draw"

def make_tts_string_from_game(game):
    result = ""
    board = chess.Board()

    if game.headers["White"] and game.headers["Black"]:
        result += f"Game between: {game.headers['White']} as white, and {game.headers['Black']} as black. [[slnc 1000]]"

    for move in game.mainline_moves():
        result += "\n" + pgn_move_to_human_text(board.san(move))
        board.push(move)

    if game.headers["Result"]:
        result += "\n" + result_to_human_text(game.headers["Result"]) + "[[slnc 500]]"

    return fix_spaces(result)

def make_tts_string_from_pgn(pgn_filepath):
    pgn = chess.pgn.read_game(open(pgn_filepath))
    return make_tts_string_from_game(pgn)

def fix_spaces(text):
    return text.replace("  ", " ")

def make_tts_script_from_game(pgn_filepath):
    text = make_tts_string_from_pgn(pgn_filepath)
    print(text)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_tts_script_from_game(sys.argv[1])
    else:
        raise Exception("No pgn provided")