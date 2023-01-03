hh, mm = map(int,input().split())
mm_add = int(input())
mm_total = hh*60 + mm + mm_add
print(mm_total//60%24, mm_total%60)