def korean_number(a):
    if a == 1:
        return "일"
    elif a == 2:
        return "이"
    elif a == 3:
        return "삼"
    elif a == 4:
        return "사"
    elif a == 5:
        return "오"
    elif a == 6:
        return "육"
    elif a == 7:
        return "칠"
    elif a == 8:
        return "팔"
    elif a == 9:
        return "구"
    elif a == 10:
        return "십"
    else:
        print("유효하지 않은 값입니다.")
b = korean_number(3)
print(b)