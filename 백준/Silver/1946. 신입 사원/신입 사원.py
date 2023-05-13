import sys


i_t = int(input())
for test_case in range(i_t):
    i_n = int(input())
    ls_applicants = [tuple(map(int, sys.stdin.readline().split())) for applicant in range(i_n)]
    ls_applicants.sort()
    cnt = 0
    score_2_min = 1e9
    for applicant in ls_applicants:
        if applicant[1] < score_2_min:
            cnt += 1
            score_2_min = applicant[1]
    print(cnt)