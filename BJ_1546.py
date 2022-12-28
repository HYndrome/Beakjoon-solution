import sys
a = sys.stdin.readline()
aa = [int(x) for x in sys.stdin.readline().split()]
bb = [y/max(aa)*100 for y in aa]
print(sum(bb)/len(bb))