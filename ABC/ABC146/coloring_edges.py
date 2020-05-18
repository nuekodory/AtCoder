from collections import defaultdict


num_node = int(input())

num_edge_by_node = defaultdict(int)
edges = []

for i in range(1, num_node):
    src, dest = map(int, input().split())
    num_edge_by_node[src] += 1
    num_edge_by_node[dest] += 1
    edges.append((src, dest))

edges.sort()
colors = defaultdict(set)

src, dest = edges.pop(0)
colors[src].add(1)
colors[dest].add(1)
palette = {1, }

for (src, dest) in edges:
    taken = set()
    if colors[src]:
        taken.union(colors[src])
    if colors[dest]:
        taken.union(colors[src])

    if palette.difference(taken):
        print(palette.difference(taken).pop())
    else:
        new_color = max(palette)+1
        print(new_color)
        palette

print(max(num_edge_by_node.values()))

