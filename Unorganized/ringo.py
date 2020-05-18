input_line = input().split()
num_divide = int(input_line[0])
smallest_of = int(input_line[1])

if num_divide == 0:
    counter = 0
    current_num = 0
    while counter < smallest_of:
        current_num += 1
        if current_num % 100 == 0:
            continue
        else:
            counter += 1

elif num_divide == 1:
    counter = 0
    current_num = 0
    while counter < smallest_of:
        current_num += 100
        if current_num % 10000 != 0 and current_num % 1000000 != 0:
            counter += 1


else:               # num_divide == 2
    counter = 0
    current_num = 0
    while counter < smallest_of:
        current_num += 10000
        if current_num % 1000000 != 0:
            counter += 1

print(str(current_num))

