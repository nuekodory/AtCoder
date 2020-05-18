from collections import defaultdict


num_room, num_path = map(int, input().split(' '))

paths = defaultdict(set)
for i in range(0, num_path):
    src, dest = map(int, input().split(' '))
    paths[src].add(dest)
    paths[dest].add(src)

rooms = {1}
route = {}

while rooms:
    new_rooms = set()
    for src in rooms:
        dest_set = paths[src]
        for dest in dest_set:
            if dest in route.keys():
                continue
            route[dest] = src
            new_rooms.add(dest)
    rooms = new_rooms

for i in range(2, num_room+1):
    if i not in route.keys():
        print("No")
        exit(0)

print("Yes")
for i in range(2, num_room+1):
    print(route[i])
