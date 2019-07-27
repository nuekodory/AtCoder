from math import ceil


num_travel, num_parallel = map(int, input().split(' '))

timings = []
for _ in range(0, num_travel):
    timings.append([int(x) for x in input().split(' ')])

costs = []
for _ in range(0, num_travel):
    costs.append([int(x) for x in input().split(' ')])

current = 0
for timing, cost in zip(timings, costs):
    # print(current, timing, cost)

    start_times = [t * ceil(current / t) for t in timing]
    actual_costs = [cos + wait for cos, wait in zip(cost, start_times)]
    selected_cost = min(actual_costs)
    current = selected_cost
    # print(selected_cost)

print(current)
exit(0)
