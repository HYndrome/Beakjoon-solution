import sys
vc = int(sys.stdin.readline())
for i in range(vc):
    vh, vw, vn = map(int, sys.stdin.readline().split())
    if vn%vh == 0:
        print(vh*100 + vn//vh)
    else:
        print(vn%vh*100 + vn//vh +1)