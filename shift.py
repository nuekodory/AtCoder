input_num = input()
input_line = input().split()
count_divide = 0

shifts = []
for input_num_str in input_line:
    if input_num_str == "0":
        shifts.append(0)
    else:
        input_num_bin = str(bin(int(input_num_str)))
        for index, char in enumerate(reversed(input_num_bin)):
            if char == '1':
                shifts.append(index)
                break

print(str(min(shifts)))



