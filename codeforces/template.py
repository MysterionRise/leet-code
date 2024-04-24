import decimal
import random
import heapq
import bisect
import math
import sys
import time

from collections import deque, Counter
from decimal import Decimal, getcontext
from functools import lru_cache
from itertools import combinations, permutations, accumulate

input = sys.stdin.readline
printf = sys.stdout.write


# nextint = sys.stdin.read

# Function to get the next token from stdin
def next():
    while True:
        token = sys.stdin.read(1)
        if token.isspace():
            continue
        break
    return token


# Function to get the next integer from stdin
def nextInt():
    num_str = next()
    while True:
        char = sys.stdin.read(1)
        if char.isspace() or char == '':
            break
        num_str += char
    return int(num_str)


# Function to get the next double from stdin
def nextDouble():
    return float(next())


def solve():
    pass


if __name__ == '__main__':
    num_of_tests = nextInt()
    for _ in range(num_of_tests):
        solve()
