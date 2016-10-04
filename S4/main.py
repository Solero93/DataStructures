import sys

MIN_HEAP_SIZE = 100000
if sys.getrecursionlimit() < MIN_HEAP_SIZE:
    sys.setrecursionlimit(MIN_HEAP_SIZE)