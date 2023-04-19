# https://www.youtube.com/watch?v=gcuZ_VGIcn4
# https://www.youtube.com/watch?v=1Bh6DBcKgOc&t=269s

i_n = int(input())
cnt_answer = 0

# 같은 열에 존재하는지 확인하는 hashset (인덱스는 열 기준)
hashset_column = [0] * i_n
# 오른쪽 하단 대각선에 존재하는지 확인하는 hashset (x + y)
#  i_n이 4일 경우 인덱스는 0 1 2 3 4 5 6
hashset_diagonal_1 = [0] * (2 * i_n - 1)
# 왼쪽 하단 대각선에 존재하는지 확인하는 hashset (x - y) 
#  i_n이 4일 경우 인덱스는 0 1 2 3 -3 -2 -1
hashset_diagonal_2 = [0] * (2 * i_n - 1)

# r 행에 퀸 놓기
def put_queen(y):
    global cnt_answer
    # i_n개의 퀸을 i_n개의 행에 모두 놓는데 성공했을 경우, cnt_answer 1 증가
    if y == i_n:
        cnt_answer += 1
        return
    # 행 내 순회
    # 아래 hashset을 이용하여 겹침 여부를 판단할 경우 인덱스만 활용하므로 시간복잡도가 O(1)
    for x in range(i_n):
        # 해당 방문이 같은 열 및 모든 대각선으로 겹치지 않았을 때,
        if not hashset_column[x] and not hashset_diagonal_1[x + y] and not hashset_diagonal_2[x - y]:
            # 방문 처리
            hashset_column[x] = hashset_diagonal_1[x + y] = hashset_diagonal_2[x - y] = 1
            # 다음 행로 이동
            put_queen(y + 1)
            # 겹치는 것이 확인되었을 경우 방문 처리를 취소
            hashset_column[x] = hashset_diagonal_1[x + y] = hashset_diagonal_2[x - y] = 0

# 0 번째 행부터 방문 시작
put_queen(0)
# 결과 출력
print(cnt_answer)