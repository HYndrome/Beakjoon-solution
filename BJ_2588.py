#변수 지정 a는 정수 b는 문자열
a = int(input())
b = input()
#b 리스트화 일의 자리수부터
b_num=[]
for i in range(len(b)-1,-1,-1):
    b_num.append(b[i])
#자릿수 별 계산값 출력
for j in range(len(b_num)):
    print(a*int(b_num[j]))
#최종 결과 출력    
print(a*int(b))