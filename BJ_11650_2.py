# lyho1127의 풀이
answer = []

for t in range(int(input())):
    x = list(map(int, input().split()))
    answer.append(x)
    

answer.sort(key = lambda x: (x[0], x[1]))

for i in answer:

    i = ' '.join(map(str, i))
    print(i)