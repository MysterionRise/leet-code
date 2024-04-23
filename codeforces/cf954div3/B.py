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
    n = nextInt()
    m = nextInt()
    arr = [[-100 for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i][j] = nextInt()
    notFound = True
    while notFound:
        notFound = False
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if arr[i][j] > arr[i - 1][j] and arr[i][j] > arr[i + 1][j] and \
                        arr[i][j] > arr[i][j - 1] and arr[i][j] > arr[i][
                    j + 1]:
                    arr[i][j] = max(arr[i - 1][j], arr[i + 1][j],
                                    arr[i][j - 1], arr[i][j + 1])
                    notFound = True
                    break
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            printf(f"{arr[i][j]} ")
        print()


if __name__ == '__main__':
    num_of_tests = nextInt()
    for _ in range(num_of_tests):
        solve()
