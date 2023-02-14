i_n, i_m = map(int, input().split())
ls_tree = [i_1 for i_1 in map(int, input().split())]
start = 0
end = max(ls_tree)
while True:
    mid = (start + end + 1) // 2
    if start == mid:
        break
    if sum(i_2 - mid for i_2 in ls_tree if i_2 - mid > 0) >= i_m:
        start = mid
    else:
        end = mid - 1
print(mid)