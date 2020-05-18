len_arr = int(input())
arr = [int(x) for x in input().split(' ')]

diffs = [arr[i] - arr[i+1] for i in range(0, len_arr-1)]
# print(diffs)

cont = 0
max_len = 0
for d in diffs:
    if d >= 0:
        cont += 1
    else:
        max_len = max(max_len, cont)
        cont = 0
else:
    max_len = max(max_len, cont)

print(max_len)
exit(0)
