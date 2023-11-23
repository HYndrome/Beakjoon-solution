# heap
import heapq

def add_10min(input_time):
    """문자열로 받은 시간에 10분을 추가하여 문자열 시간으로 return하는 함수"""
    hour, minute = map(int, input_time.split(':'))
    # 50분 이상이었을 경우 분 처리
    if minute >= 50:
        hour += 1
        minute = minute - 50
    else:
        minute += 10
    # 자리 수 처리
    if hour < 10:
        str_hour = '0' + str(hour)
    else:
        str_hour = str(hour)
    if minute < 10:
        str_minute = '0' + str(minute)
    else:
        str_minute = str(minute)
    out_time = str_hour + ':' + str_minute    
    return out_time

def solution(book_time):
    # 입실 시간 순으로 정렬
    book_time.sort(key=lambda x:(x[0], x[1]))
    # 객실 배열
    heap_room = []
    for each_book_time in book_time:
        start_time = each_book_time[0]
        # 끝나는 시간은 퇴실 기준으로 10분 청소
        end_time = add_10min(each_book_time[1])
        # 객실 배열이 비었을 경우, 객실 추가 (최초 시작)
        if not heap_room:
            heapq.heappush(heap_room, end_time)
        else:
            # 객실 배열 중, 가장 일찍 끝나는 시간이 새로운 예약의 시작시간보다 늦을 경우, 새로운 객실 추가
            if heap_room[0] > start_time:
                heapq.heappush(heap_room, end_time)
            # 객실 배열 중, 가장 일찍 끝나는 시간이, 새로운 예약의 시작시간보다 빠를 경우, 해당 객실 갱신
            else:
                heapq.heappop(heap_room)
                heapq.heappush(heap_room, end_time)
    # 객실 수 return    
    print(heap_room)
    return len(heap_room)