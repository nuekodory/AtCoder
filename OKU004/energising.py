from collections import deque


num_task, num_energizer, max_energizing, energy = map(int, input().split(' '))

tasks = [int(x) for x in input().split(' ')]
initial_drinks = [int(x) for x in input().split(' ')]

tasks.sort()
initial_drinks.sort(reverse=True)
drinks = deque(initial_drinks[:max_energizing])

num_drinking = 0

for index, task in enumerate(tasks):
    # drinking
    while drinks and task > energy:
        num_drinking += 1
        energy += drinks.popleft()

    if task > energy:
        print("No")
        print(max(index, 0))
        exit(0)
    else:
        energy -= task

print("Yes")
print(num_drinking)
exit(0)
