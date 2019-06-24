number, taste_base = map(int, input().split(' '))

pie_all = int(number * ((number + 1) / 2 + taste_base - 1))

taste_range = range(taste_base, taste_base + number)
taste_range_abs = [abs(i) for i in taste_range]
abs_min = min(taste_range_abs)
minimum = 0

if abs_min in taste_range:
    minimum = abs_min
else:
    minimum = -abs_min

print(pie_all - minimum)
