i_n = int(input())
ls_chem = list(map(int, input().split()))
ls_chem.sort()
sum_chem = 0
start = 0 
end = i_n - 1
record = [2e9, 0, 0]
while start != end:
    gap = abs(ls_chem[start] + ls_chem[end])
    if gap < record[0]:
        record = [gap, ls_chem[start], ls_chem[end]]
        if gap == 0:
            break
    if abs(ls_chem[start + 1] + ls_chem[end]) >= abs(ls_chem[start] + ls_chem[end - 1]):
        end -= 1
    else:
        start += 1
print(record[1], record[2])