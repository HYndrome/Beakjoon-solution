# import sys

# i_n = int(sys.stdin.readline())
# lst_i = list(map(int, sys.stdin.readline().split()))
# set_i = set(lst_i)
# lst_i2 = list(set_i)
# lst_i2.sort()
# for i_1 in lst_i:
#     print(lst_i2.index(i_1), end = " ")

# # set 자료형은 순서가 없어서 인덱스가 없다.
# # 시간 초과

import sys

i_n = int(sys.stdin.readline())
lst_i = list(map(int, sys.stdin.readline().split()))
set_i = set(lst_i)
lst_i2 = list(set_i)
lst_i2.sort()
lst_seq = [i_1 for i_1 in range(len(lst_i2))]
dict_i2_seq = {i_2 : i_3 for i_2, i_3 in zip(lst_i2, lst_seq)}

for i_4 in lst_i:
    print(dict_i2_seq[i_4], end = " ")

# 시간 1972ms
# for문으로 indexing을 하면 엄청 오래걸린다. 하나하나 찾아야하기 때문
# 그래서 indexing을 반복해서 안할 방법을 찾다가 dictionaty 자료형을 사용하니 해결되었다.