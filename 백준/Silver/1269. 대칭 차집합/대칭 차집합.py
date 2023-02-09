i_a, i_b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
set_sym = set_a ^ set_b
print(len(set_sym))