# 전체 경우의 수 압축, combinations
from itertools import combinations

# ('INFP', 'INFP', 'ESTP') 형태를 받아, 
# 3명 간의 심리거리 계산 return하는 함수
def distance_calculator(students):
    distance_sum = 0
    for i in range(4):
        if students[0][i] != students[1][i]:
            distance_sum += 1
        if students[1][i] != students[2][i]:
            distance_sum += 1
        if students[2][i] != students[0][i]:
            distance_sum += 1
    return distance_sum
# 입력
i_t = int(input())
for case in range(i_t):
    i_n = int(input())
    students = list(input().split())
    # 한 종류의 mbti가 3이 넘어가면 의미가 없어지므로 {'mbti': 수} 형태로 저장
    dict_student = {}
    for student in students:
        dict_student[student] = dict_student.get(student, 0) + 1
        # 같은 mbti 3명 이상일 경우 나머지에 관계 없이 출력은 0
        if dict_student[student] == 3:
            break
    if max(dict_student.values()) == 3:
        print(0)
    # 다시 딕셔너리를 개별 mbti.의 리스트 형태로 돌리고, 최대 16*2 명
    # 32명에서 3명을 뽑는 경우의 수 진행 32C3 - 충분히 반복 가능한 수
    # 각 조합별 거리를 구해서 최소 거리를 구함
    else:
        new_students = []
        for student_mbti in dict_student:
            for values in range(dict_student[student_mbti]):
                new_students.append(student_mbti)
        distance_min = 12
        for student_combination in combinations(new_students, 3):
            distance_combination = distance_calculator(student_combination)
            if distance_combination < distance_min:
                distance_min = distance_combination
        print(distance_min)