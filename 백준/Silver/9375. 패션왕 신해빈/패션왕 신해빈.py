import sys

# 옷 종류 별 수가 딕셔너리 형태로 주어질 경우, 
# 알몸이 아닌 상태로 의상을 입을 수 있는 경우 출력하는 함수
def clothes_combination_counter(closet):
    # 한 종류의 옷을 선택할 수 있는 개수 = 해당 종류 옷 개수 + 1 (안입는 경우)
    cnt = 1
    for cnt_sort in closet.values():
        cnt *= cnt_sort + 1
    # 모든 경우의 수 - 1 (모든 옷 안입는 경우)
    return cnt - 1

# 입력
i_t = int(sys.stdin.readline())
for case in range(i_t):
    # {옷 종류: 종류별 옷 개수} 형태로 딕셔너리 저장
    closet = {}
    i_n = int(sys.stdin.readline())
    for clothes in range(i_n):
        clothes_name, clothes_sort = sys.stdin.readline().split()
        closet[clothes_sort] = closet.get(clothes_sort, 0) + 1
    # 연산 및 출력
    print(clothes_combination_counter(closet))
