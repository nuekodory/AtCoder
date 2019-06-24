n = int(input())

nums = map(int, input().split(' '))

arr = sorted(nums)
print(arr[-4:])

num_zeros = 0
num_pos = 0
num_neg = 0

for num in arr:
    if num > 0:
        num_pos += 1
    elif num < 0:
        num_neg += 1
    else:
        num_zeros += 1

# all pos or zero
if num_neg == 0:
    print(sum(arr) - arr[0] * 2)
    lhs = arr[0]

    for i in range(1, n-1):
        rhs = arr[i]
        cal = lhs - rhs
        print(str(lhs) + " " + str(rhs))
        lhs = cal

    print(str(arr[n-1]) + " " + str(lhs))
    exit(0)

# all neg or zero
elif num_pos == 0:
    print(-sum(arr) + arr[n-1] * 2)
    lhs = arr[n-1]

    for i in reversed(range(0, n-1)):
        rhs = arr[i]
        cal = lhs - rhs
        print(str(lhs) + " " + str(rhs))
        lhs = cal
    exit(0)

# 0 and pos / 0 and neg / pos and neg (and 0)
else:
    plus_index = 0
    for index, num in enumerate(arr):
        if num < 0:
            continue
        else:
            plus_index = index
            break

    print(-sum(arr[:plus_index]) + sum(arr[plus_index:]))

    if len(arr) == 2:
        print(str(arr[1]) + " " + str(arr[0]))
        exit(0)

    lhs = arr[plus_index]
    for i in reversed(range(1, plus_index)):
        rhs = arr[i]
        cal = lhs - rhs
        print(str(lhs) + " " + str(rhs))
        lhs = cal

    print(str(arr[0]) + " " + str(lhs))
    lhs = arr[0] - lhs

    for i in range(plus_index+1, n-1):
        rhs = arr[i]
        cal = lhs - rhs
        print(str(lhs) + " " + str(rhs))
        lhs = cal

    print(str(arr[n-1]) + " " + str(lhs))
    exit(0)
