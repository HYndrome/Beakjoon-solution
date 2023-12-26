i_t = int(input())
for tc in range(i_t):
    test_no = int(input())
    scores = list(map(int, input().split()))
    dct_scores = {}
    for score in scores:
        dct_scores[score] = dct_scores.get(score, 0) + 1
    ls_score_cnt = list(dct_scores.items())
    ls_score_cnt.sort(key=lambda x: (-x[1], -x[0]))
    print(f"#{test_no} {ls_score_cnt[0][0]}")
