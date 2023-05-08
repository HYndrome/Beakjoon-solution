import sys
from collections import deque


i_n = int(input())

ls_meeting = [tuple(map(int, sys.stdin.readline().split())) for _ in range(i_n)]
ls_meeting.sort(key=lambda x : (x[1], x[0]))
que_meeting = deque(ls_meeting)

cnt = 0
end_time_room = 0
while que_meeting:
    start_time, end_time = que_meeting.popleft()
    if start_time >= end_time_room:
        cnt += 1
        end_time_room = end_time
print(cnt)