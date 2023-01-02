def recursion(s, l, r):
    if l >= r: return 1, l + 1
    elif s[l] != s[r]: return 0, l + 1
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

i_t = int(input())
for i_1 in range(i_t):
    s_i = input()
    i_o1, i_o2 = isPalindrome(s_i)
    print(i_o1, i_o2)