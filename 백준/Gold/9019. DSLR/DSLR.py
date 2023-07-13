import sys
from collections import deque

# 정수를 입력 받고, DSLR 연산 결과를 {"D": 222, "S": 110, ...} 형태의 딕셔너리로 리턴하는 함수
def dslr(num):
    # "D" 연산 계산
    cal_d = (num * 2) % 10000
    # "S" 연산 계산
    cal_s = num - 1
    if num == 0:
        cal_s = 9999
    # "L"과 "R" 을 deque.rotate 이용해서 연산 계산
    #  zfill(n)은 길이가 n이 될 때까지 문자열 왼쪽에 0 추가
    num_str = str(num).zfill(4)
    cal_l = int(num_str[1:4] + num_str[0])
    cal_r = int(num_str[3] + num_str[0:3])
    return {"D": cal_d, "S": cal_s, "L": cal_l, "R": cal_r}

# BFS 로 최단 거리 탐색
def dslr_tracker(start, end):
    # 방문을 저장하는 딕셔너리, { 방문한곳, 방문연산 } 형태로 저장
    visited = {}
    que = deque([start])
    while que:
        current = que.popleft()
        for cal, result in dslr(current).items():
            # print(cal, result)
            # 시작과 도착점이 같을 경우 의미 없는 연산 횟수 +1 이 되므로 탐색에서 제외
            if not visited.get(result) and result != current:
                que.append(result)
                visited[result] = visited.get(current, "") + cal
                # print(visited)
                if result == end:
                    return visited[result]

# 입력
i_t = int(sys.stdin.readline())
for case in range(i_t):
    start, end = map(int, sys.stdin.readline().split())
    # 출력
    print(dslr_tracker(start, end))