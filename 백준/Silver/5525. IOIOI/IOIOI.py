# 입력
i_n = int(input())
i_m = int(input())
s_s = input()
# 비교문자열
s_p = "IO" * i_n + "I"
# s_p 카운팅용 변수
cnt = 0
# 문자열 인덱스로 비교
for i in range(0, i_m - 2*i_n):
    if s_s[i:i+2*i_n+1] == s_p:
        cnt += 1
# 출력
print(cnt)