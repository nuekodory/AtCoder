num_travel = int(input())

route = []
for i in range(0, num_travel):
    input_line = input().split()
    input_int = list(map(int, input_line))
    route.append((input_int[0], input_int[1], input_int[2]))

t = 0
x = 0
y = 0
for i in range(0, num_travel):
    next_t, next_x, next_y = route[i]
    distance = abs(next_x - x) + abs(next_y - y)
    travel_time = next_t - t
    if travel_time < distance or (travel_time - distance) % 2 == 1:
        print("No")
        exit(0)
    t = next_t
    x = next_x
    y = next_y
else:
    print("Yes")
