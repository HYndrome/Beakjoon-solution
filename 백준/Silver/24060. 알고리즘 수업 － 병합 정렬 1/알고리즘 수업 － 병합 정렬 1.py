def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high + 1) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                lst_record.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                lst_record.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            lst_record.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            lst_record.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

i_n, i_k = map(int, input().split())
lst_input = list(map(int, input().split()))
lst_record = []
lst_sorted = merge_sort(lst_input)
if i_k > len(lst_record):
    print(-1)
else:
    print(lst_record[i_k - 1])