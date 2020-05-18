num_knight = int(input())

monsters = [int(x) for x in input().split(' ')]
knights = [int(x) for x in input().split(' ')]

initial_num_monster = sum(monsters)

for pos, power in enumerate(knights):
    if monsters[pos] <= power:
        defeated = monsters[pos]
        monsters[pos] = 0
        rest_power = power - defeated
    else:
        monsters[pos] -= power
        continue

    monsters[pos+1] = max(monsters[pos+1] - rest_power, 0)

rest_monster = sum(monsters)
print(initial_num_monster - rest_monster)
exit(0)
