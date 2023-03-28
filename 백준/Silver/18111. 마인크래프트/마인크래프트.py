import sys

dct_ground = {}

i_n, i_m, i_b = map(int, sys.stdin.readline().split())
for i_1 in range(i_n):
    ls_input = map(int, sys.stdin.readline().split())
    for i_2 in ls_input:
        dct_ground[i_2] = dct_ground.get(i_2, 0) + 1

# print(dct_ground)
ls_result = []
for ground_target in range(min(dct_ground.keys()), max(dct_ground.keys()) + 1):
    result_b = i_b
    result_t = 0
    for ground_height, ground_cnt in dct_ground.items():
        if ground_height > ground_target:
            result_t += 2 * (ground_height - ground_target) * ground_cnt
            result_b += (ground_height - ground_target) * ground_cnt
        else:
            result_t += (ground_target - ground_height) * ground_cnt
            result_b -= (ground_target - ground_height) * ground_cnt            
    if result_b >= 0:
        ls_result.append((ground_target, result_t))

result = min(ls_result, key = lambda x: (x[1], -x[0]))
print(result[1], result[0])