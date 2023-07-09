import sys

# 테스트 케이스 수 입력
i_t = int(sys.stdin.readline())

# [1,2,3] 형태의 문자열을 정수를 포함하는 리스트로 변경해주는 함수
def make_intlist(s_input):
    result = s_input.strip("[]")
    result = result.split(",")
    if result == [""]:
        result = []
    else:
        result = list(map(int, result))       
    return result

# 정수를 포함하는 리스트를 [1,2,3] 형태의 문자열로 변경해주는 함수
def make_outputformat(l_output):
    l_str_output = map(str, l_output)
    output = "[" + ",".join(l_str_output) +"]"
    return output
    
# 문자열 수행함수와 정수포함리스트를 입력 받고, 출력조건으로 출력하는 함수
def ac(commands, l_input):
    start = 0
    end = len(l_input) - 1
    # 정방/ 역방 상태 표시 변수
    reverse = False
    # 문자열 수행함수 처리
    for command in commands:
        # "R" 입력 받을 경우 , 불린 reverse 토글
        if command == "R":
            if reverse == False:
                reverse = True
            else:
                reverse = False
        # "D" 입력 받을 경우 불린 reverse에 따라 처리
        if command == "D":
            if reverse == False:
                start += 1
            else:
                end -= 1
    # 결과 처리
    # 배열이 비어 있는데 D를 사용한 경우 end < start 
    if end - start < -1:
        print("error")
    # 불린 reverse에 따라 결과 처리 및 문자열 변경, 출력
    else:
        if reverse == False:
            result = l_input[start:end + 1]
        else:
            result = list(reversed(l_input[start:end + 1]))
        result = make_outputformat(result)
        print(result)

# 테스트 케이스 반복문
for case in range(i_t):
    # 수행 함수 입력
    s_p = sys.stdin.readline().rstrip()
    # 배열의 수
    i_n = int(sys.stdin.readline())
    # 배열 입력
    s_x = sys.stdin.readline().rstrip()
    # 입력 배열 처리
    l_x  = make_intlist(s_x)
    # 문제 처리
    ac(s_p, l_x)