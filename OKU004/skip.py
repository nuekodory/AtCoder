num_cell = int(input())
cells = [int(x) for x in input().split(' ')]

if num_cell == 1:
    print(0)
    exit(0)

statement = None
num_change = 0

for i in range(1, num_cell):
    if cells[i] == cells[i-1]:
        continue
    is_increasing = cells[i] > cells[i-1]

    if statement is is_increasing:
        continue
    else:
        num_change += 1
        statement = is_increasing

if statement is None:
    print(0)
else:
    print(num_change+1)

exit(0)
