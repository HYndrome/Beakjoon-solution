import sys
a = int(sys.stdin.readline())
for i in range(a):
    result = sys.stdin.readline()
    num1 = 0
    score = 0
    for j in result:
        if j == "O":
            num1 += 1
            score += num1
        else:
            num1 = 0
    print(score)