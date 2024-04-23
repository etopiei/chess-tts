import os
import sys
import chess.pgn
import hashlib
import subprocess
from make_transcript import make_tts_string_from_game

def make_files(base_dir, out_dir, max_moves):
    for file in os.listdir(base_dir):
        if ".pgn" in file:
            pgn = open(base_dir + "/" + file)
            games = []
            while True:
                game = chess.pgn.read_game(pgn)
                if game is not None:
                    games.append(game)
                else:
                    break

            for game in games:
                if len(list(game.mainline_moves())) < (max_moves * 2):
                    text_result = make_tts_string_from_game(game)
                    filename = hashlib.md5(text_result.encode()).hexdigest()
                    subprocess.call(['say', '-v', 'Samantha', text_result, '-o', f"{out_dir}/{filename}.aiff"]) 

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python make_audio_files.py <BASE_DIR> <OUT_DIR> (MAX_MOVES)\ne.g. python make_audio_files.py '~/Download/Lichess Elite Database' audio_games")
    else:
        base_dir = sys.argv[1]
        out_dir = sys.argv[2]
        max_moves = 300
        if len(sys.argv) > 3:
            max_moves = int(sys.argv[3])

        make_files(base_dir, out_dir, max_moves)
