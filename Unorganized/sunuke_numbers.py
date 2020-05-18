def sunuke_sum_div(arg: int) -> int:
    sum_digit = 0
    arg_str = str(arg)
    for char in arg_str:
        sum_digit += int(char)
    return sum_digit / arg


# main
num_sunuke_sum = int(input())

for i in range(1, num_sunuke_sum+1):
    num_nines = (i - 1) // 9
    num_first = i - num_nines * 9

    this_arg = str(num_first)
    for j in range(0, num_nines):
        this_arg += "9"

    this_num = int(this_arg)
    this_sunuke = sunuke_sum_div(this_num)

    print(this_arg, this_sunuke)
