len_arr = int(input())
arr = list(map(int, input().split(' ')))

bins = ['{:061b}'.format(x) for x in arr]

one_in_digits = [sum([int(b[digit]) for b in bins]) for digit in reversed(range(0, 61))]

sum_top_digit = one_in_digits[61]

if sum_top_digit and sum_top_digit % 2 == 0:
    start_digit = 62
else:
    start_digit =