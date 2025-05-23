"""Sunfish chess engine."""

version = "sunfish 2023"

from .constants import initial
from .board import Position
from .uci import uci_loop

# Create initial position
init_pos = Position(initial, 0, (True, True), (True, True), 0, 0)

def main():
    """Start the UCI interface."""
    uci_loop(init_pos, version)

if __name__ == "__main__":
    main()
