# 파이썬의 round()는 정확한 반올림이 아니다...!
# 짝수에 가까운 수를 반환 round(2.5) = 2
import sys

def round_int(number):
    numleft = number % 1
    if numleft >= 0.5:
        return int(number) + 1
    else:
        return int(number)


# 입력
i_n = int(sys.stdin.readline())
# 의견 개수 0 처리
if i_n == 0:
    difficulty = 0
else:
    scores = []
    for i in range(i_n):
        score = int(sys.stdin.readline())
        scores.append(score)
    # 정렬
    scores.sort()
    # 절사평균 범위 구하기
    i_cut = round_int(i_n * 15 / 100)
    scores = scores[0 + i_cut: i_n - i_cut]
    # 평균 계산
    difficulty = round_int(sum(scores) / len(scores))
# 출력
print(difficulty)