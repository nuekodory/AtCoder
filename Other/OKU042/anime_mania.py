num_program, time_wake = map(int, input().split(' '))

programs = [(tuple(map(int, reversed(input().split(' ')))), i+1) for i in range(0, num_program)]

programs.sort(reverse=True)
print(programs)

t = time_wake
leap = 0

for program in programs:
    (end, start), index = program
    print(index, start, end)
    if t < end:
        leap += end - t
    t = start

leap += time_wake - t
print(leap)
