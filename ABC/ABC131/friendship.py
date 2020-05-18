import itertools


num_vertex, target = map(int, input().split(' '))

# ensure num_vertex >= 3
if num_vertex == 2:
    if target == 0:
        print("1")
        print("1 2")
    else:
        print("-1")

    exit(0)

edges = [(1, i) for i in range(2, num_vertex+1)]
appendable_edges = list(itertools.combinations(range(2, num_vertex+1), 2))

num_removal = len(appendable_edges) - target

if num_removal < 0:
    print("-1")
    exit(0)

edges.extend(appendable_edges[:num_removal])

print(len(edges))
for edge in edges:
    src, dest = edge
    print(src, dest)

exit(0)
