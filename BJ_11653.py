import sys
i_in = int(sys.stdin.readline())
if i_in == 1:
    print("")
else:
    i_c = 2
    while i_c <= i_in:
        if i_in%i_c == 0:
            print(i_c)
            i_in /= i_c
            i_c = 2
            if i_c == i_in:
                break
        else:
            i_c += 1
#이거 틀려서 3번 답으로 가니까 맞았음