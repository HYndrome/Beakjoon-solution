# 딕셔너리 자료 저장
import sys

pw_container = {}
# 입력
i_n, i_m = map(int, sys.stdin.readline().split())
for pw_input in range(i_n):
    site, pw = sys.stdin.readline().split()
    pw_container[site] = pw
# 출력
for pw_output in range(i_m):
    site_ask = sys.stdin.readline().rstrip()
    print(pw_container[site_ask])