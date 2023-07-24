# dp
import sys

i_n = int(sys.stdin.readline())
# sum_r은 r로 끝나는 최소의 비용을 저장하는 변수
sum_r = 0
sum_g = 0
sum_b = 0

for i in range(i_n):
    red, green, blue = map(int, sys.stdin.readline().split())
    # 새로운 sum_r은 sum_g과 sum_b 중 작은 값에 red의 비용을 더한 값
    sum_r, sum_g, sum_b  = min(sum_g, sum_b) + red, min(sum_r, sum_b) + green, min(sum_r, sum_g) + blue
print(min(sum_r, sum_g, sum_b))