import sys
# 각 행열 N*M 행열을 길이가 N*M인 줄줄이 리스트로 만들기
# 리스트는 제일 윗 행부터
lst_1 = []
lst_2 = []
i_n, i_m = map(int, sys.stdin.readline().split())
for i_1 in range(i_n):
    lst = list(map(int, sys.stdin.readline().split()))
    lst_1 += lst
for i_2 in range(i_n):
    lst = list(map(int, sys.stdin.readline().split()))
    lst_2 += lst
#  각 리스트를 행 단위로 리스트로 잘라서 인덱싱하여 더한 값을 출력
for i_3 in range(i_n):
    lst_print = []
    for i_4 in range(i_3*i_m, i_3*i_m + i_m):
        lst_print.append(lst_1[i_4] + lst_2[i_4])
    print(*lst_print)