a = int(input())
if a%4 != 0 :
    print(f"{a}년은 평년입니다")
else:    
    if a%100 == 0:
        if a%400 == 0:
            print(f"{a}년은 윤년입니다")
        else:
            print(f"{a}년은 평년입니다")