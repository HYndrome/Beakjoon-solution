import heapq

def time_add(time_current, time_add):
    """문자열 형태의 현재 시각과 소요 시간을 받고
    끝나는 시간을 return하는 함수"""
    time_hr, time_m = map(int, time_current.split(":"))
    time_add = int(time_add)
    time_hr += (time_m + time_add) // 60
    time_m = (time_m + time_add) % 60
    # 두자리수로 맞춰주는 과정 9:0 -> 09:00
    if len(str(time_hr)) == 1:
        time_hr = "0" + str(time_hr)
    else:
        time_hr = str(time_hr)
    if len(str(time_m)) == 1:
        time_m = "0" + str(time_m)
    else:
        time_m = str(time_m)
    time_end = time_hr + ":" + time_m
    return time_end

print(time_add("09:00", "1"))

def time_sub(time_current, time_next):
    """문자열 형태의 현재 시각과 다음 시간을 받고
    그 시간의 차이를 return하는 함수"""
    current_hr, current_m = map(int, time_current.split(":"))
    next_hr, next_m = map(int, time_next.split(":"))
    return (next_hr - current_hr)*60 + (next_m - current_m)

def solution(plans):
    answer = []
    heap_plans = []
    plans_stack = []

    # 과제 시작 시간이 빠른 것을 처리할 수 있도록 heap 사용
    for plan in plans:
        heapq.heappush(heap_plans, [plan[1], plan[2], plan[0]])
    # 과제 순환
    while heap_plans:
        # 현재 과제 기준
        current = heapq.heappop(heap_plans)
        sparetime = 0
        # 다음 과제가 남아있을 때
        if heap_plans:
            # 다음 과제 전까지 현재 과제를 처리할 수 있는 경우
            if time_add(current[0], current[1]) <= heap_plans[0][0]:
                # 과제 처리 완료 처리
                answer.append(current[2])
                # 여분 시간 처리
                sparetime += time_sub(current[0], heap_plans[0][0]) - int(current[1])
                # 여분 시간을 모두 소모하여 처리하지 못한 과제를 최근 순으로 처리(stack)
                while sparetime > 0 and plans_stack:
                    # 여분 시간으로 처리하지 못한 과제를 처리할 수 있을 경우
                    if plans_stack[-1][1] <= sparetime:
                        sparetime -= plans_stack[-1][1]
                        answer.append(plans_stack[-1][0])
                        plans_stack.pop()
                    # 여분 시간으로 처리하지 못한 과제를 처리할 수 없을 경우
                    else:
                        plans_stack[-1][1] = plans_stack[-1][1] - sparetime
                        sparetime = 0
            # 다음 과제 전까지 현재 과제를 처리할 수 없는 경우 처리하지 못한 과제에 stack
            else:
                plans_stack.append([current[2], int(current[1]) - time_sub(current[0], heap_plans[0][0])])
        # 다음 과제가 없을 경우 현재 과제는 완료 처리
        else:
            answer.append(current[2])
    # 처리하지 못한 과제는 stack에서 최근 순으로 처리
    while plans_stack:
        lastest = plans_stack.pop()
        answer.append(lastest[0])
        
    return answer