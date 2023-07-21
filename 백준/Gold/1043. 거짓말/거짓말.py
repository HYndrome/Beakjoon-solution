# bfs 완전 탐색
from collections import deque

# 입력
i_n, i_m = map(int, input().split())
# 초기 진실 아는 사람
killers = deque(map(int, input().split()))
killers.popleft()
# 각 사람별 연결관계를 나타내는 그래프 (같은 파티에 한번이라도 참여했으면 연결)
graph_party = [[] for person in range(i_n + 1)]
# 입력된 파티 저장 리스트
parties = []
for party in range(i_m):
    # 각 파티별 참여인원 입력
    participants = deque(map(int, input().split()))
    participants.popleft()
    parties.append(participants)
    # 각 사람별 연결관계 그래프 입력
    for participant in participants:
        for companion in participants:
            if companion != participant and companion not in graph_party[participant]:
                graph_party[participant].append(companion)
# new 진실 아는 사람 저장 리스트
# A가 진실을 아는 사람일 경우,
# A와 B, B와 C가 각각 같은 파티에 참여할 경우,
# A,B,C 모두 진실된 이야기를 알게 됨
# 따라서 완전 탐색 문제가 됨
# 완전 탐색 결과를 저장할 그래프
new_killers = [False] * (i_n + 1)
# bfs / 시작점은 초기 진실아는 사람
for killer in killers:
    new_killers[killer] = True
    que = deque([killer])
    while que:
        current = que.popleft()
        for companion in graph_party[current]:
            if new_killers[companion] == False:
                new_killers[companion] = True
                que.append(companion)
# 최종 과장된 이야기를 할 수 있는 파티 개수 = new 진실 아는 사람이 없는 파티 개수
cnt_survive = 0
for party in parties:
    for participant in party:
        if new_killers[participant] == True:
            break
    else:
         cnt_survive += 1
# 출력
print(cnt_survive)