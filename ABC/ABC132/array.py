num_input = int(input())

arr = [int(s) for s in input().split(' ')]

meet_cond = 0
for i in range(0, num_input-3+1):
    x, y, z = arr[i], arr[i+1], arr[i+2]

    if min(x, y, z) == y or max(x, y, z) == y:
        pass
    else:
        meet_cond += 1

print(meet_cond)
