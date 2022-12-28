def judge_group(input):
    count_a = [0 for x in range(97,123)]
    for i in range(len(input)):
        chr_1 = input[i]
        count_a[ord(chr_1)-97] += 1 
        if count_a[ord(chr_1)-97] >= 2 and input[i] == input[i-1]:
            count_a[ord(chr_1)-97] -= 1
    if max(count_a) >= 2:
        return False
    else:
        return True
num1 = int(input())
answer = 0
for k in range(num1):
    str1 = input()
    if judge_group(str1) == True:
        answer += 1
print(answer)