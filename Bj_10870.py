import sys

def pibo_num(k_1):
    if k_1 == 0:
        return 0
    elif k_1 == 1:
        return 1
    else:
        a = pibo_num(k_1 -1) + pibo_num(k_1 -2)
        return a

i_n = int(sys.stdin.readline())
print(pibo_num(i_n))