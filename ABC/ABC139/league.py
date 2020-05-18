num_player = int(input())
table = [{i: int(x)-1 for i, x in enumerate(input().split(' ') + [str(num_player)])} for _ in range(0, num_player)]
# print(table)

ptr = [0 for _ in range(0, num_player)]

count = 0
available = set(range(0, num_player))

while min(ptr) != num_player-1:
    count += 1
    blocker = set()
    for i in available:
        target = table[i][ptr[i]]
        if target > i:
            continue
        if target not in available:
            continue
        if target == num_player:
            available.remove(target)
            continue
        if table[target][ptr[target]] == i:
            if target in blocker or i in blocker:
                continue
            ptr[i] += 1
            ptr[target] += 1
            blocker.add(i)
            blocker.add(target)
    if not blocker:
        print(-1)
        exit(0)

print(count)
exit(0)
