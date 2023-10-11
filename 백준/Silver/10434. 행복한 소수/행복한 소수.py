# 10000 이하 소수 찾기
import sys

# 소수 저장 리스트
ls_sosu = [False] * 2 + [True] * 9999
for i in range (2, 10001):
    if ls_sosu[i] == True:
        i_multi = 2 * i
        while i_multi <= 10000:
            ls_sosu[i_multi] = False
            i_multi += i
    else:
        continue

# 행복한수 확인 함수
def find_happy(num:int):
    """
    정수를 입력 받아서 해당 수가 행복한 수일 경우 True, 아닐 경우 False를 반환
    """
    ls_happy = [False] * 325
    result = False
    def cal_happy(num):
        nonlocal result
        happy_sum = 0
        while num > 0:
            num_digit = num % 10
            happy_sum += num_digit**2
            num //= 10
        if happy_sum == 1:
            result = True
        else:
            if ls_happy[happy_sum] == True:
                return
            else:
                ls_happy[happy_sum] = True
                cal_happy(happy_sum)
    cal_happy(num)
    return result

# 케이스 입력 받기
i_p = int(sys.stdin.readline())
for i in range(i_p):
    i_test, i_input = map(int, sys.stdin.readline().split())
    s_result = ""
    # 소수 확인
    if ls_sosu[i_input] == False:
        s_result = "NO"
    else:
        # 행복한수 확인
        if find_happy(i_input) == False:
            s_result = "NO"
        else:
            s_result = "YES"
    # 값 출력 
    print(i_test, i_input, s_result)