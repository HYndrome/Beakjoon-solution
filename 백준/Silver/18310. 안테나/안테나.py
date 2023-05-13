i_n = int(input())
ls_house = list(map(int, input().split()))
ls_house.sort()
print(ls_house[(i_n - 1) // 2])