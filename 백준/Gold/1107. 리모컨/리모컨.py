from itertools import product

# 입력 받기
i_n = int(input())
i_m = int(input())
# i_m이 0인 경우 추가로 입력 받지 않음
ls_m = []
if i_m != 0:
    ls_m += list(map(int, input().split()))
ls_control = [str(i) for i in range(10) if i not in ls_m]
# case1. 리모컨으로 입력 가능한 수조합으로 i_n과 가장 가까운 수와 i_n과의 차이
# 가장 가까운 수는 i_n과 자리 수가 1 차이 나는 수
digit = len(str(i_n))
s_n = str(i_n)
# 만약 ls_control 내의 수로 i_n을 조합 가능하다면 가장 작은 수는 i_n의 자릿수 길이
consistency = True
for s in s_n:
    if s not in ls_control:
        consistency = False
        break
if consistency == True:
    min_1 = len(s_n)
else:
    # 조합이 불가능할 경우 
    min_1 = 500000
    for i in [digit -1 , digit, digit + 1]:
        if i > 0:
            # iteration tools의 product 기능으로 가능한 조합을 튜플로 만듦
            ls_product = list(product(ls_control, repeat=i))
            for result_p in ls_product:
                # 그 튜플을 문자열로 합치고 정수 변환
                i_result_p = int(''.join(result_p))
                # 리모콘을 눌러야하는 횟수 = i_n과 만들어진 수 차이 + 만들어진 수의 자릿수
                d_p = abs(i_n - i_result_p) + i
                # 최솟값 갱신
                if d_p < min_1:
                    min_1 = d_p

# case2. 처음 지점 100과 i_n과의 차이
current = 100
# case1과 case2 중 작은 값이 최종값
min_2 = abs(i_n - current)
print(min(min_1, min_2))