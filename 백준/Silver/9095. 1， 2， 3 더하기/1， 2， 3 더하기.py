# 테스트 케이스 수 i_n 입력 받기
i_n = int(input())
# 전체 수 입력 받기
# 반복 연산을 줄이기 위해서 입력 받은 수 중 가장 큰 수를 입력 받아 그 수만큼 DP
ls_input = []
for i in range(i_n):
    ls_input.append(int(input()))
input_max = max(ls_input)
# 가장 큰 수가 2이하일 경우 3까지 형성
if input_max <= 2:
    input_max = 3
# DP 값 저장할 빈 리스트 형성
ls_123 = [0] * (input_max + 1)
# 시작값
ls_123[1] = 1
ls_123[2] = 2
ls_123[3] = 4
# DP 적용
for n in range(4, input_max + 1):
    ls_123[n] = ls_123[n - 1] + ls_123[n - 2] + ls_123[n - 3]
# 한 번에 값 출력
for num in ls_input:
    print(ls_123[num])
