import sys

# M,N,x,y 를 받고 몇 번째인지 구하는 함수
def inka(i_m, i_n, i_x, i_y):
    # i_m이 i_n 보다 큰 경우만을 고려, 반대일 경우에는 M과N, x와y를 서로 바꿈
    if i_n < i_m:
        i_m, i_n = i_n, i_m
        i_x, i_y = i_y, i_x
    # 몇 번째인지 확인하는 변수
    cnt = i_x
    # 연산수를 줄이기 위해서
    # 전체 경우의 수는 M * (어떤수) + x 의 경우만 고려
    while True:
        # 현재 수 (cnt)를 N으로 나눈 나머지가 y를 N으로 나눈 나머지와 같다면
        if cnt % i_n == i_y % i_n:
            # 값 출력
            return cnt
        # 아닐 경우 x + M
        else:
            cnt += i_m
        # M * N까지 반복을 했다면 (사실 최대 공배수가 더 좋음)
        if cnt > i_m * i_n:
            # 유효하지 않은 값 판단 및 return
            return -1    

# 테스트 케이스별 반복 입력
i_t = int(sys.stdin.readline())
for case in range(i_t):
    i_m, i_n, i_x, i_y = map(int, sys.stdin.readline().split())
    # 출력
    print(inka(i_m, i_n, i_x, i_y))
