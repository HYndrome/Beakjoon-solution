import sys
n = int(sys.stdin.readline())
for i in range(n):
	l = list(map(int, sys.stdin.readline().split()))
	cnt = l[0]
	scores = l[1:]
	avg = sum(scores) / len(scores)
	j = 0
	for score in scores:
		if score > avg: j = j + 1
	print(format(j / cnt, "2.3%"))