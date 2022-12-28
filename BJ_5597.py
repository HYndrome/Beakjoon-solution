import sys
bb_s = set([x for x in range(1,31)])
aa = []
for i in range(28):
    a = int(sys.stdin.readline())
    aa.append(a)
aa_s = set(aa)
print(min(bb_s-aa_s))
print(max(bb_s-aa_s))