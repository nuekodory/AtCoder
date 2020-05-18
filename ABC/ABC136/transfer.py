max_1, water_1, water_2 = map(int, input().split(' '))

transfer = min(water_2, max_1 - water_1)
print(water_2 - transfer)
exit(0)
