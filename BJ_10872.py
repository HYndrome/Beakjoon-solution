import sys

def factorial(k):
    if k == 1 or k == 0:
        return 1
    else:
        return k * factorial(k-1)

i_i = int(sys.stdin.readline())
print(factorial(i_i))