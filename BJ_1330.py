#input 정수로 받기
a_input, b_input = input().split()
a = int(a_input)
b = int(b_input)
#if문을 이용한 조건에 따른 출력
if a > b:
    print(">")
else:
    if a < b:
        print("<")
    else:
        print("==")