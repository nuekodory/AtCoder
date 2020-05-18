import math
import itertools
from collections import defaultdict


seq_count, initial_number = map(int, input().split(' '))

sequence = list(map(int, input().split(' ')))

sequence.sort(reverse=True)
# print(sequence)

seq_limited = [item for item in sequence if item < initial_number]
k_count = math.factorial(seq_count) // math.factorial(seq_count - (len(sequence) - len(seq_limited)))
# print(k_count)

calculation_perm_to_count = defaultdict(int)

for perm in itertools.permutations(seq_limited):
    smallest_mod_num = 100001
    calculation_perm_list = []
    for mod_num in perm:
        if mod_num < smallest_mod_num:
            calculation_perm_list.append(mod_num)
            smallest_mod_num = mod_num

    calculation_perm = tuple(calculation_perm_list)
    calculation_perm_to_count[calculation_perm] += k_count

sum_mods = 0

# print(calculation_perm_to_count)

for calc_perm, count in calculation_perm_to_count.items():
    num = initial_number
    for mod_num in calc_perm:
        num = num % mod_num
    sum_mods += num * count

sum_mods = sum_mods % (10**9 + 7)

print(sum_mods)
exit(0)
