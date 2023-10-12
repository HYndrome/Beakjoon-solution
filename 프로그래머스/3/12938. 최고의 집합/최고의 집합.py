def solution(n, s):
    i_div = s // n
    i_rest = s % n
    answer = []
    if i_div == 0:
        answer = [-1]
    else:
        for i in range(n - i_rest):
            answer.append(i_div)
        for i in range(i_rest):
            answer.append(i_div + 1)
    return answer