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


def calculate_total_distance(y, x1, x2, x3):
    return abs(x1 - y) + abs(x2 - y) + abs(x3 - y)


def solve():
    x1, x2, x3 = map(int, input().strip().split(" "))
    min_val = 100000
    for y in range(1, 11):
        min_val = min(min_val, calculate_total_distance(y, x1, x2, x3))
    print(min_val)


if __name__ == '__main__':
    num_of_tests = int(input().strip())
    for _ in range(num_of_tests):
        solve()