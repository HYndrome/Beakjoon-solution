# 움직일 수 있는 방향 딕셔너리 설정
dct_move = {
    'LT': (-1, -1), 'T': (0, -1), 'RT': (1, -1),
    'L': (-1, 0), 'R': (1, 0),
    'LB': (-1, 1), 'B': (0, 1), 'RB': (1, 1)
}
# 체스판 빈 리스트 형성
lst_chess = [[0]*8 for i_1 in range(8)]
# 체스판 입력: 실제 리스트 내 좌표 딕셔너리 설정
dct_col = {
    '8': 0, '7': 1, '6': 2, '5': 3,
    '4': 4,  '3': 5, '2': 6 , '1': 7 
    }
dct_row = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4,  'F': 5, 'G': 6 , 'H': 7 
    }
# 입력 받기, 이동 명령은 리스트로 저장
s_index_k, s_index_s, s_move = input().split()
lst_move_his = []
for i_1 in range(int(s_move)):
    lst_move_his.append(input())
# 처음 위치 x, y로 분리해서 저장
x_k = dct_row[s_index_k[0]]
y_k = dct_col[s_index_k[1]]
x_s = dct_row[s_index_s[0]]
y_s = dct_col[s_index_s[1]]
# 명령별로 이동
for s_1 in lst_move_his:
    # 킹 이동하기
    x_k += dct_move[s_1][0]
    y_k += dct_move[s_1][1]
    # 킹이 체스판에서 벗어났을 경우, 롤백
    if (x_k < 0) + (x_k > 7) + (y_k < 0) + (y_k > 7):
        x_k -= dct_move[s_1][0]
        y_k -= dct_move[s_1][1]
    # 돌 옮기기, 돌은 킹과 좌표가 겹쳤을 때, 킹만큼 이동   
    if (x_k == x_s) * (y_k == y_s):
        x_s += dct_move[s_1][0]
        y_s += dct_move[s_1][1]
    # 돌이 체스판에 벗어났을 경우, 킹과 돌 둘다 롤백    
    if (x_s < 0) + (x_s > 7) + (y_s < 0) + (y_s > 7):
        x_k -= dct_move[s_1][0]
        y_k -= dct_move[s_1][1]
        x_s -= dct_move[s_1][0]
        y_s -= dct_move[s_1][1]
# 딕셔너리에서 value 기준으로 키 값을 찾기
k_final_x = [key_1 for key_1, value_1 in dct_row.items() if value_1 == x_k]
k_final_y = [key_2 for key_2, value_2 in dct_col.items() if value_2 == y_k]
s_final_x = [key_3 for key_3, value_3 in dct_row.items() if value_3 == x_s]
s_final_y = [key_4 for key_4, value_4 in dct_col.items() if value_4 == y_s]
# 출력, 언패킹
print(*k_final_x, *k_final_y, sep= '')
print(*s_final_x, *s_final_y, sep= '')