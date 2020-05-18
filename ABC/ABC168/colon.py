import math


length_hour, length_min, hour, minute = map(int, input().split(' '))
total_min = hour * 60 + minute

hx = math.sin((total_min / (12 * 60)) * (2 * math.pi)) * length_hour
hy = math.cos((total_min / (12 * 60)) * (2 * math.pi)) * length_hour
mx = math.sin((minute / 60) * (2 * math.pi)) * length_min
my = math.cos((minute / 60) * (2 * math.pi)) * length_min

distance = math.sqrt((hx - mx) ** 2 + (hy - my) ** 2)

print(f"{distance}")
