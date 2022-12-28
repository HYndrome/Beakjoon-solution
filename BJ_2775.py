v_case = int(input())
for i in range(v_case):
    vk = int(input())
    vn = int(input())
    lst_0 = [i+1 for i in range(vn)]
    for j in range(vk):
        for k in range(vn-1, 0, -1):
            lst_0[k] = sum(lst_0[0:k+1])
    print(lst_0[vn-1])