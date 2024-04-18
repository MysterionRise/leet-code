import sys
import math
from collections import deque, Counter
from typing import List, Callable

input = sys.stdin.readline
printf = sys.stdout.write


def next():
    while True:
        token = sys.stdin.read(1)
        if not token.isspace():
            break
    return token


def nextInt():
    num_str = next()
    while True:
        char = sys.stdin.read(1)
        if char.isspace() or char == '':
            break
        num_str += char
    return int(num_str)


def nextDouble():
    return float(next() + sys.stdin.readline().strip())


class MultiHashSet:
    def __init__(self):
        self.map = Counter()

    def count(self, x):
        return self.map[x]

    def add(self, x):
        self.map[x] += 1

    def remove(self, x):
        if self.map[x] == 0:
            return False
        self.map[x] -= 1
        if self.map[x] == 0:
            del self.map[x]
        return True

    def __str__(self):
        return f"MultiHashSet({dict(self.map)})"


class MultiTreeSet:
    def __init__(self):
        self.map = {}

    def count(self, x):
        return self.map.get(x, 0)

    def add(self, x):
        self.map[x] = self.count(x) + 1

    def first(self):
        return min(self.map.keys())

    def last(self):
        return max(self.map.keys())

    def remove(self, x):
        prev = self.count(x)
        if prev == 0:
            return False
        if prev == 1:
            del self.map[x]
        else:
            self.map[x] = prev - 1
        return True


class SegmentTree:
    def __init__(self, values: List[int],
                 commutative: Callable[[int, int], int], zero: int):
        self.n = len(values)
        self.t = [zero] * (2 * self.n)
        self.t[self.n:] = values
        self.commutative = commutative
        self.zero = zero
        self.build()

    def build(self):
        for i in range(self.n - 1, 0, -1):
            self.t[i] = self.commutative(self.t[2 * i], self.t[2 * i + 1])

    def modify(self, p: int, x: int):
        pos = p + self.n
        self.t[pos] = x
        while pos > 1:
            self.t[pos // 2] = self.commutative(self.t[pos], self.t[pos ^ 1])
            pos //= 2

    def query(self, left: int, right: int):
        res = self.zero
        l, r = left + self.n, right + self.n
        while l < r:
            if l & 1:
                res = self.commutative(res, self.t[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.commutative(res, self.t[r])
            l //= 2
            r //= 2
        return res


def solve():
    c = nextInt()
    v0 = nextInt()
    v1 = nextInt()
    a = nextInt()
    l = nextInt()

    pos = 0
    ans = 0
    while pos < c:
        if ans > 0:
            pos += min(v1, v0 + ans * a) - l
        else:
            pos += v0
        ans += 1

    print(ans)


if __name__ == '__main__':
    solve()