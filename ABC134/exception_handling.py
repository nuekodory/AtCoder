from collections import Counter


len_arr = int(input())

arr = [int(input()) for _ in range(0, len_arr)]

counter = Counter(arr)
arr_max = max(counter)

if counter[arr_max] == 1:
    max_index = arr.index(arr_max)
    for i in range(0, len_arr):
        if i == max_index:
            del(counter[arr_max])
            print(max(counter))
        else:
            print(arr_max)

else:
    for _ in range(0, len_arr):
        print(arr_max)

exit(0)
