import heapq
def solution(jobs):
    answer = 0
    now = 0
    start = -1
    cnt_job = 0
    heap_process = []
    while cnt_job < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap_process, [job[1], job[0]])
        if len(heap_process) > 0:
            current  = heapq.heappop(heap_process)
            start = now
            now += current[0]
            answer += now - current[1]
            cnt_job += 1
        else:
            now += 1
    return answer // len(jobs)