# dp
import sys

# N 저장리스트
ls_n = []
# 정삼각형 변 저장 리스트 (dp용)
ls_wave = [0, 1, 1, 1, 2]
# 입력
i_t = int(sys.stdin.readline())
for case in range(i_t):
    i_n = int(sys.stdin.readline())
    ls_n.append(i_n)
# 모든 N 중 최대 값까지 ls_wave dp로 계산 
max_n = max(ls_n)
current = len(ls_wave)
while current <= max_n:
    wave_current = ls_wave[current - 1] + ls_wave[current - 5]
    ls_wave.append(wave_current)
    current += 1
# 출력
for i_n in ls_n:
    print(ls_wave[i_n])    
