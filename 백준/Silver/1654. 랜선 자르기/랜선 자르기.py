import sys

i_k, i_n = map(int, sys.stdin.readline().split())
ls_lan = [int(sys.stdin.readline()) for _ in range(i_k)]

def lan_cutter(list , object):
    total_lan = 0
    for lan in list:
        total_lan += lan // object
    return total_lan

ls_result = []
def binery_search(start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if lan_cutter(ls_lan, mid) < i_n:
        binery_search(start, mid - 1)
    else:
        binery_search(mid + 1, end)
        ls_result.append(mid)

binery_search(1, 2**31 - 1)
print(max(ls_result))