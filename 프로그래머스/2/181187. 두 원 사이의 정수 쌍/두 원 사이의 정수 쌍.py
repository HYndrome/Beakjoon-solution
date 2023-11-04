import math

def solution(r1, r2):
    answer = 0
    # 축 위의 점
    answer += 4 * (r2 - r1 + 1)
    # 축 위가 아닌 점
    for y in range(1, r2):
        not_axis = 0
        if y < r1:
            x2 = math.floor((r2**2 - y**2)**0.5)
            x1 = math.ceil((r1**2 - y**2)**0.5)
            not_axis += x2 - x1 + 1
        else:
            x2 = math.floor((r2**2 - y**2)**0.5)
            not_axis += x2
        answer += 4 * not_axis
    return answer