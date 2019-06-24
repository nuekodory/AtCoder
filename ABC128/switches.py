import itertools
from collections import defaultdict


possible_numbers = [0, 1]
num_switch, num_lamp = map(int, input().split(' '))

lamp_connection = defaultdict(list)
for i in range(0, num_lamp):
    divided_input = input().split(' ')
    del(divided_input[0])
    connected_switches = [int(x)-1 for x in divided_input]

    for switch in connected_switches:
        lamp_connection[switch].append(i)

mods = tuple(map(int, input().split(' ')))

trials = itertools.product(possible_numbers, repeat=num_switch)


num_success = 0
for switch_state in trials:
    sums = defaultdict(int)
    for index, statement in enumerate(switch_state):
        targets = lamp_connection[index]
        for target in targets:
            sums[target] += statement

    for i in range(0, num_lamp):
        if sums[i] % 2 != mods[i]:
            break
    else:
        num_success += 1

print(num_success)
exit(0)
