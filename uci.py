"""UCI protocol interface."""

import time
from .constants import parse, render
from .searcher import Searcher
from .board import Move, Position

def uci_loop(init_pos, version):
    """Main UCI protocol interaction loop."""
    hist = [init_pos]
    searcher = None

    while True:
        args = input().split()
        
        if not args:
            continue
            
        if args[0] == "quit":
            break

        elif args[0] == "uci":
            print("id name", version)
            print("uciok")

        elif args[0] == "isready":
            print("readyok")

        elif args[:2] == ["position", "startpos"]:
            del hist[1:]
            for ply, move in enumerate(args[3:]):
                i, j = parse(move[:2]), parse(move[2:4])
                prom = move[4:].upper() if len(move) > 4 else ""
                if ply % 2 == 1:  # Apply rotation for black's moves
                    i, j = 119 - i, 119 - j
                hist.append(hist[-1].move(Move(i, j, prom)))

        elif args[0] == "go":
            # Parse timing information
            wtime, btime, winc, binc = [int(a) / 1000 for a in args[2::2]]
            # Adjust time for the current side to move
            if len(hist) % 2 == 0:
                wtime, winc = btime, binc
            # Calculate thinking time
            think = min(wtime / 40 + winc, wtime / 2 - 1)
            
            # Initialize new searcher for this move
            searcher = Searcher()
            start = time.time()
            move_str = None
            
            # Start iterative deepening search
            for depth, gamma, score, move in searcher.search(hist):
                # Update best move if we have improved the score
                if score >= gamma:
                    i, j = move.i, move.j
                    if len(hist) % 2 == 0:  # Rotate coordinates for black
                        i, j = 119 - i, 119 - j
                    move_str = render(i) + render(j) + move.prom.lower()
                    print("info depth", depth, "score cp", score, "pv", move_str)
                
                # Stop if we're close to our allocated time
                if move_str and time.time() - start > think * 0.8:
                    break
            
            print("bestmove", move_str or '(none)')
