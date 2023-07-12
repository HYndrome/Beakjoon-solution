# 최소힙과 최대힙을 두 개를 동시에 계산
import sys, heapq

# 연산 문자와 정수를 받고 최소힙, 최대힙을 계산하는 함수
def d_heap(op_type, op_num):
    # 데이터 삽입 연산
    if op_type == "I":
        heapq.heappush(l_min_heap, op_num)
        heapq.heappush(l_max_heap, -op_num)
        # 딕셔너리에 op_num: 개수 꼴로 저장
        dict_num[op_num] = dict_num.get(op_num, 0) + 1
    # 데이터 삭제 연산
    if op_type == "D":
        if dict_num:
            popchecker = False
            # 최소 제거
            if op_num < 0:
                # dict_num 에서 value를 1을 감소시킬 key를 찾을 때까지 
                # l_min_heap 내에서 heappop 반복
                while popchecker == False:
                    num_min = heapq.heappop(l_min_heap)
                    if dict_num.get(num_min):
                        dict_num[num_min] -= 1
                        if dict_num[num_min] == 0:
                            dict_num.pop(num_min)
                        popchecker = True
            # 최대 제거
            if op_num > 0:
                while popchecker == False:
                    num_max = - heapq.heappop(l_max_heap)
                    if dict_num.get(num_max):
                        dict_num[num_max] -= 1
                        if dict_num[num_max] == 0:
                            dict_num.pop(num_max)
                        popchecker = True
                  
# 데이터 입력 
i_t = int(sys.stdin.readline())
for case in range(i_t):
    i_k = int(sys.stdin.readline())
    # 최소힙 최대힙 리스트
    l_min_heap = []
    l_max_heap = []
    dict_num = {}
    # 힙 길이 세는 변수
    for op in range(i_k):
        op_type, op_num = sys.stdin.readline().split()
        op_num = int(op_num)
        # 연산 적용
        d_heap(op_type, op_num)
    # 빈 리스트일 경우 / 아닐 경우 출력 처리
    # 마지막 최대 최소 출력은 전체 수를 정리하고 있는 dict_num 이용 
    if dict_num:
        print(max(dict_num), min(dict_num))
    else:
        print("EMPTY")
