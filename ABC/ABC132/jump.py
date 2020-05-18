def jump(to, dst, num_move):
    if dest == to:
        return num_move
    else:
        pass


num_node, num_edge = map(int, input().split(' '))

lines = [input().split(' ') for _ in range(0, num_edge)]
edges = [(int(line[0]), int(line[1])) for line in lines]

src, dest = map(int, input().split(' '))

graph = {i: set() for i in range(1, num_node+1)}
for edge in edges:
    s, d = edge
    graph[s].add(d)

