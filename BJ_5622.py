def trans_atn(a):
    if a in ["A", "B", "C"]:
        return 2
    elif a in ["D","E", "F"]:
        return 3
    elif a in ["G","H", "I"]:
        return 4
    elif a in ["J","K", "L"]:
        return 5
    elif a in ["M","N", "O"]:
        return 6
    elif a in ["P","Q", "R", "S"]:
        return 7
    elif a in ["T","U", "V"]:
        return 8
    elif a in ["W","X", "Y", "Z"]:
        return 9
    elif a in ["D","E", "F"]:
        return 9
    else:
        return 0
a = input()
num_lst = []
for i in range(len(a)):
    num_lst.append(trans_atn(a[i]))
print(sum(num_lst)+len(a))
