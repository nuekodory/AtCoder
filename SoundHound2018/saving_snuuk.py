import copy


def travel(_from: int, _to: int, _destination: list, _visited: list, _cost: list):

    if (_from, _to) in _visited:
        return

    visited = copy.deepcopy(_visited)
    visited.append((_from, _to))

    destination = copy.deepcopy(_destination)
    destination.append(_to)

    cost = copy.deepcopy(_cost)

    cost.append(costs[(_from, _to)])

    if _to == city_to:
        routes.append((destination, cost))
        return

    for to_city in lines[_to]:
        travel(_to, to_city, destination, visited, cost)


input_line = input().split()

num_cities = int(input_line[0])
num_lines = int(input_line[1])
city_from = int(input_line[2])
city_to = int(input_line[3])

lines = {}
costs = {}

for _ in range(0, num_lines):
    input_line = input().split()
    line_from = int(input_line[0])
    line_to = int(input_line[1])
    cost_yen = int(input_line[2])
    cost_snuuk = int(input_line[3])
    costs[(line_from, line_to)] = (cost_yen, cost_snuuk)
    costs[(line_to, line_from)] = (cost_yen, cost_snuuk)

    if line_from in lines.keys():
        lines[line_from].append(line_to)
    else:
        lines[line_from] = [line_to]

    if line_to in lines.keys():
        lines[line_to].append(line_from)
    else:
        lines[line_to] = [line_from]

routes = []

for first_destination in lines[city_from]:
    travel(city_from, first_destination, [city_from], [], [])

for year in range(0, num_cities):
    valid_routes = []
    maximum_cost = 10 ** 15 + 1

    for visited_list, cost_list in routes:
        for index, exchange_on in enumerate(visited_list):
            if exchange_on <= year:
                continue

            paid = 0
            for i in range(0, index):
                yen, snuuk = cost_list[i]
                paid += yen
            for i in range(index, len(cost_list)):
                yen, snuuk = cost_list[i]
                paid += snuuk
            if paid > maximum_cost:
                continue

            valid_routes.append((paid, index, visited_list))
            maximum_cost = paid

    print(str(10 ** 15 - maximum_cost))
