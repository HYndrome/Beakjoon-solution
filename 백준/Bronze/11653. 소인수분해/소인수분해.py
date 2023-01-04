import sys
i_in = int(sys.stdin.readline())
if i_in == 1:
    print("")
else:
    i_c = 2
    while i_in != 1:
        if i_in%i_c == 0:
            print(i_c)
            i_in /= i_c
        else:
            i_c += 1