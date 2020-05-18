num_month, day_per_month = map(int, input().split(' '))

ans = 0
for month in range(4, num_month+1):
    ans += len([day for day in range(22, day_per_month+1)
                if day // 10 >= 2 and day % 10 >= 2 and (day // 10) * (day % 10) == month])

print(ans)
exit(0)
