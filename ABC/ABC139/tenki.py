forecasts = [c for c in input().strip()]
weather = [c for c in input().strip()]

ans = 0
for f, w in zip(forecasts, weather):
    ans += int(f == w)

print(ans)
exit(0)
