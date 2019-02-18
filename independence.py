input_line = input().split()
num_city = int(input_line[0])
num_road = int(input_line[1])

road_dict = {}
for i in range(0, num_road):
    input_line = input().split()
    road_from = int(input_line[0])
    road_to = int(input_line[1])

    if road_from in road_dict:
        road_dict[road_from].append(road_to)
    else:
        road_dict[road_from] = [road_to]

    if road_to in road_dict:
        road_dict[road_to].append(road_from)
    else:
        road_dict[road_to] = [road_from]

print(road_dict)


