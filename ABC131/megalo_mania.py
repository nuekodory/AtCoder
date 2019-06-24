num_task = int(input())

maps = [map(int, input().split(' ')) for _ in range(0, num_task)]
tasks = [(b, a) for a, b in maps]
tasks.sort()


current_time = 0

for deadline, time_needed in tasks:
    end_time = current_time + time_needed

    if end_time > deadline:
        print("No")
        break

    current_time = end_time

else:
    print("Yes")
