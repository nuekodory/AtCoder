# main

input_str = input()
input_num = int(input_str)

input_num_digits = len(input_str) - 1

if input_num == 10 ** input_num_digits:
    min_digit_sums = [10]

else:
    former_num = 10 ** input_num_digits
    latter_num = input_num - former_num

    digit_sum = 0
    for char in str(former_num):
        digit_sum += int(char)
    for char in str(latter_num):
        digit_sum += int(char)
    min_digit_sums = [digit_sum]

for i in range(1, input_num // 2):
    former_num = i
    latter_num = input_num - i

    digit_sum = 0
    for char in str(former_num):
        digit_sum += int(char)
    if digit_sum >= min(min_digit_sums):
        continue
    for char in str(latter_num):
        digit_sum += int(char)
    if digit_sum < min(min_digit_sums):
        min_digit_sums.append(digit_sum)

print(str(min(min_digit_sums)))


