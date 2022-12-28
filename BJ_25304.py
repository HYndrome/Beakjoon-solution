# 준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 
# 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.
# 영수증에 적힌,
# 구매한 각 물건의 가격과 개수, 구매한 물건들의 총 금액을 보고, 
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
# 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
# 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.

# 입력값 받기
total_price = int(input())
total_category = int(input())
total_lst = []
for i in range(total_category):
    lst = list(map(int,input().split()))
    total_lst.append(lst)
# 입력값 계산
total_category_price = []
for j in total_lst:
        price_multi = j[0]*j[1]
        total_category_price.append(price_multi)
total_price_cal = sum(total_category_price)
# 계산값과 입력값 비교
if total_price == total_price_cal:
    print("Yes")
else:
    print("No")