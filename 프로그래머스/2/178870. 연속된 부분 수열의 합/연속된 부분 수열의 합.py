def solution(sequence, k):
    start = 0
    end = 0
    L = len(sequence)
    sum_total = sequence[start]
    len_current = 1000001
    answer = []
    while start < L and end < L:
        if sum_total < k:
            end += 1
            if end < L:
                sum_total += sequence[end]
        elif sum_total > k:
            sum_total -= sequence[start]
            start += 1
        else:
            if end - start + 1 < len_current:
                answer = [start, end]
                len_current = end - start + 1
            if start == end:
                break
            sum_total -= sequence[start]
            start += 1
    return answer