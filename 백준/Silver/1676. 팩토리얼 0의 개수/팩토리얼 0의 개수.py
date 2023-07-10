# 입력
i_n = int(input())
# 팩토리얼 계산
i_factorial = 1
for i in range(1, i_n + 1):
    i_factorial *= i
# 0이 아닌 수 찾기
s_factorial = str(i_factorial)
for i in range(1, len(s_factorial) + 1):
    if s_factorial[-i] != "0":
        print(i - 1)
        break