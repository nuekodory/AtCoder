def sum_of_digits(arg: int) -> int:
    arg_str = str(arg)
    sum_digits = 0
    for char in arg_str:
        sum_digits += int(char)

    return sum_digits


# main
input_num = int(input())

if input_num % sum_of_digits(input_num) == 0:
    print("Yes")
else:
    print("No")
