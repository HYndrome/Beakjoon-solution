num1 = int(input())
result = []
for i in range(num1):
    num2, num3 = map(int,input().split())
    sum1 = num2 + num3
    result.append(sum1)
for j in result:
    print(j)