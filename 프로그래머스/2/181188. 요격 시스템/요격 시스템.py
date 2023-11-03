# targets의 범위 (0 ≤ s < e ≤ 100,000,000) 때문에 heap 사용
import heapq

def solution(targets):
    """각 폭격 미사일의 x 좌표 범위 목록 targets이 매개변수로 주어질 때, 모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟값을 return
    """
    # heap 적용 (미사일의 끝을 음수로 하여 끝 범위가 큰 것부터 heappush)
    heap_missles = []
    for missile in targets:
        start, end = missile[0], missile[1]
        heapq.heappush(heap_missles, [start, -end])
    # answer; 필요한 요격 수, current 현재 요격 처리 가능한 최대 가능 지점
    answer = 0
    current = 0
    # heappop으로 미사일 pop
    for i in range(len(heap_missles)):
        start, end = heapq.heappop(heap_missles)
        # 요격 불가능할 경우; 요격 수 추가, 처리 가능 지점 수정
        if start >= current:
            current = -end
            answer += 1
        # 요격 시; 처리 가능 지점 수정
        if -end < current:
            current = -end
    return answer