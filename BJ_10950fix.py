count_input = int(input())
list_result=[]
for i in range(count_input):
    a_input, b_input = map(int,input().split())
    e = a_input + b_input
    list_result.append(e)
for j in range(len(list_result)):
    print(list_result[j])