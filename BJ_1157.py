str_origin = input()
def count_upper(a):
    a_upper = a.upper()
    count_upper = []
    for i in range(65, 91):
        sum1 = a_upper.count(chr(i))
        count_upper.append(sum1)
    if count_upper.count(max(count_upper)) >= 2:
        return "?"
    else:
        max_value = chr(count_upper.index(max(count_upper))+65)
        return max_value
answer = count_upper(str_origin)
print(answer)