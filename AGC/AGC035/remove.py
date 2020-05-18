len_arr = int(input())

arr = [int(i) for i in input().split(' ')]

while len(arr) > 2:
    print(arr)
    m = min(arr[1:-1])
    i = arr.index(m, 1, -1)
    arr.pop(i)
    arr[i] += m
    arr[i-1] += m

print(arr)
print(sum(arr))

