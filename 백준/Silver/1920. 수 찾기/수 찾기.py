i_n = int(input())
st_n = set(i_1 for i_1 in map(int, input().split()))
i_m = int(input())
for i_2 in map(int, input().split()):
    if i_2 in st_n:
        print(1)
    else:
        print(0)