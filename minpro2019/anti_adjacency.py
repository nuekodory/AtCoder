n, k = map(int, input().split(' '))

max_density = k * 2 - 1

if n >= max_density:
    print("YES")
else:
    print("NO")
exit(0)
