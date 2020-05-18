from collections import defaultdict


num_town, num_collect = map(int, input().split(' '))

paths = [set()] * num_town
for _ in range(0, num_town-1):
    x, y = map(int, input().split(' '))
    src = min(x, y)
    dest = max(x, y)
    paths[src].add(dest)

photos = [int(x) for x in input().split(' ')]

parent = {}
depths = {1: 0}

root = 1
current = 0

dest_set = paths[root]
for dest in dest_set:
    depths[dest] = current+1
    parent[dest] = root
