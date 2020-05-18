num_box, num_key = map(int, input().split(' '))

by_box = {b: [] for b in range(1, num_box+1)}
by_fit = {}

for _ in range(1, num_key+1):
    cost, num_open = map(int, input().split(' '))
    unlock = tuple([int(x) for x in input().split(' ')])

    if unlock in by_fit.keys():
        former_cost = by_fit[unlock]
        if former_cost <= cost:
            continue
        else:
            for b in unlock:
                by_box[b].remove((former_cost, unlock))
                by_box[b].append((cost, unlock))
    else:
        for b in unlock:
            by_box[b].append((cost, unlock))

# print(by_box)
for b in range(1, num_box+1):
    if len(by_box[b]) == 0:
        print("-1")
        exit(0)
    by_box[b].sort()
# print(by_box)

# one-by-one
limit = 0
one_opened = set()
for b in range(1, num_box+1):
    if b in one_opened:
        continue
    cost, unlock = by_box[b][0]
    limit += cost
    one_opened = one_opened.union(unlock)

print(limit)

