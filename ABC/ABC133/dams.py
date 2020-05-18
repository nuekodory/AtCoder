num_mount = int(input())

dam = [int(s) for s in input().split(' ')]

even = [i for index, i in enumerate(dam) if index % 2 == 0]
odds = [i for index, i in enumerate(dam) if index % 2 == 1]

sum_even = sum(even)
sum_odds = sum(odds)

mount = [sum_even - sum_odds]

dam.append(dam[0])
for i in range(0, num_mount-1):
    mount.append(2 * dam[i] - mount[i])

mount_str = map(str, mount)
print(' '.join(mount_str))
