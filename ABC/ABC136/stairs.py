num_cell = int(input())

heights = [int(x) for x in input().split(' ')]

heights[0] -= 1

for i in range(1, num_cell):
    if heights[i-1] < heights[i]:
        heights[i] -= 1
    elif heights[i-1] > heights[i]:
        break
else:
    print("Yes")
    exit(0)

print("No")
exit(0)
