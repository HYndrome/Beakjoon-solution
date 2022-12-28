import sys
import math
A, B, C = map(int, sys.stdin.readline().split())
# 손익 분기점: A + B*t =< C*t
def profit(a, b, c):
    if c > b:
        t = a / (c - b) + 1
        t = math.floor(t)
        print(t)
    else:
        print("-1")
profit(A, B, C)