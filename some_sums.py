input_line = input().split()
max_value = int(input_line[0])
min_sum = int(input_line[1])
max_sum = int(input_line[2])

values = []

for value in range(1, max_value + 1):
    value_str = str(value)
    number_sum = 0
    for number_char in value_str:
        number_sum += int(number_char)

    if min_sum <= number_sum <= max_sum:
        values.append(value)

print(str(sum(values)))
