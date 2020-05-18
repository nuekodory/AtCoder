import copy


input_line = input().split()
grid_size = int(input_line[0])
num_color = int(input_line[1])

differential_cost = {}
for color_from in range(1, num_color + 1):
    input_line = input().split()
    for color_to in range(1, num_color + 1):
        differential_cost[(color_from, color_to)] = int(input_line[color_to-1])

color_map = {}
for x in range(1, grid_size + 1):
    input_line = input().split()
    for y in range(1, grid_size + 1):
        color_map[(x, y)] = int(input_line[y-1])

current_color_dict = {}
for color in range(1, num_color+1):
    current_color_dict[color] = 0

current_color_mod0 = copy.deepcopy(current_color_dict)
current_color_mod1 = copy.deepcopy(current_color_dict)
current_color_mod2 = copy.deepcopy(current_color_dict)

for index, color in color_map.items():
    x, y = index
    if (x + y) % 3 == 0:
        current_color_mod0[color] += 1
    elif (x + y) % 3 == 1:
        current_color_mod1[color] += 1
    elif (x + y) % 3 == 2:
        current_color_mod2[color] += 1

combinations = [(color_mod0, color_mod1, color_mod2)
                for color_mod0 in range(1, num_color+1)
                for color_mod1 in range(1, num_color+1)
                for color_mod2 in range(1, num_color+1)]

cost_list = []
for combination in combinations:
    color_mod0, color_mod1, color_mod2 = combination
    if color_mod0 == color_mod1 or color_mod0 == color_mod2 or color_mod1 == color_mod2:
        continue

    cost = 0
    for color_from in range(1, num_color+1):
        cost += differential_cost[(color_from, color_mod0)] * current_color_mod0[color_from]
        cost += differential_cost[(color_from, color_mod1)] * current_color_mod1[color_from]
        cost += differential_cost[(color_from, color_mod2)] * current_color_mod2[color_from]

    cost_list.append(cost)

print(str(min(cost_list)))
