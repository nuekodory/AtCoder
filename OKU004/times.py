def ans(x):
    delimiter = 10 ** 9 + 7

    if x == 0:
        return "0"
    if x % 2 == 0:
        return str(2 ** (x // 2) % delimiter)
    else:
        return str(((2 ** (x // 2 - 1)) * 3) % delimiter)


num_query = int(input())
arr = [int(x) for x in input().split(' ')]

print(' '.join(map(ans, arr)))
exit(0)
