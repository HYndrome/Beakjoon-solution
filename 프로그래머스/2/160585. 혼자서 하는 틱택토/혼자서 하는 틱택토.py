def bingo(board, string):
    """board와 문자를 입력 받고 승리 여부를 return하는 함수"""
    for y in range(3):
        for x in range(3):
            if board[y][x] != string:
                break
        else:
            return True
    for x in range(3):
        for y in range(3):
            if board[y][x] != string:
                break
        else:
            return True
    
    for i in range(3):
        if board[i][i] != string:
            break
    else:
        return True
    
    ls_cross = [[0, 2], [1, 1], [2, 0]]
    for x, y in ls_cross:
        if board[y][x] != string:
            break
    else:
        return True
    return False

def cnt_board(board, string):
    """board와 문자을 입력 받고 해당 문자의 개수를 return하는 함수"""
    cnt = 0
    for y in range(3):
        for x in range(3):
            if board[y][x] == string:
                cnt += 1
    return cnt

def solution(board):
    # 정상적인 게임
    # "O"의 개수는 "X"의 개수
    if cnt_board(board, "O") == cnt_board(board,"X"):
        # "O"가 승리했을 경우 해당 x
        if bingo(board, "O"):
            return 0
        return 1
    # "O"의 개수는 "X"의 개수 + 1
    if cnt_board(board, "O") == cnt_board(board,"X") + 1:
        # "X"가 승리했을 경우 해당 x
        if bingo(board, "X"):
            return 0
        return 1
    # 나머지는 다 비정상 게임
    return 0