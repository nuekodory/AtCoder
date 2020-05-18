len_arr = int(input())
arr = [int(x) for x in input().split(' ')]
increasing = range(1, len_arr+1)

rep_inc = 0

for i, inc in zip(arr, increasing):
    if i != inc:
        rep_inc += 1

if rep_inc == 0 or rep_inc == 2:
    print("YES")
else:
    print("NO")

exit(0)
