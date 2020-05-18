arr_input = input().strip()
arr = [c == "R" for c in arr_input]

arr_r = [0] * len(arr)
cont = 1
for i in range(1, len(arr)):
    if arr[i-1] and not arr[i]:
        arr_r[i-1] = cont
        cont = 1
    elif arr[i-1] and arr[i]:
        cont += 1
# print(arr_r)

arr_l = [0] * len(arr)
cont = 1
for i in reversed(range(1, len(arr))):
    if not arr[i] and not arr[i-1]:
        cont += 1
    if not arr[i] and arr[i-1]:
        arr_l[i] = cont
        cont = 1

# print(arr_l)

ans = [0] * len(arr)

for i in range(0, len(arr)):
    if arr_r[i]:
        side_sum = arr_r[i] + arr_l[i+1]
        med = side_sum // 2
        if side_sum % 2 == 0:
            ans[i] = med
            ans[i+1] = med
        elif arr_r[i] % 2 == 0:
            ans[i] = med
            ans[i+1] = med + 1
        else:
            ans[i] = med + 1
            ans[i+1] = med

print(" ".join(map(str, ans)))
exit(0)
