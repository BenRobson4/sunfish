#!/usr/bin/env pypy3
from __future__ import print_function

import sys
import time, math
from itertools import count
from collections import namedtuple, defaultdict
from classes.position import Move, Position
from classes.searcher import Searcher
from globals.tunings import MATE_UPPER, MATE_LOWER, QS, QS_A, EVAL_ROUGHNESS, opt_ranges
from globals.constants import A1, initial
from tools.uci import run, parse, render, uci_loop

version = "sunfish 2023"
if __name__ == "__main__":
    print("Sunfish", version, "starting up...")
    initial_position = [Position(initial, 0, (True, True), (True, True), 0, 0)]

    #input = raw_input

    # minifier-hide start
    run(sys.modules[__name__], initial_position[-1])
    sys.exit()
    # minifier-hide end

    uci_loop(initial_position, version)
