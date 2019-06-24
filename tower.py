def delta2lower_height(arg_num):
    height = 0
    for i in range(1, arg_num):
        height += i
    return height


input_line = input().split()

higher_margin = int(input_line[0])
lower_margin = int(input_line[1])

delta = higher_margin - lower_margin

lower_height = delta2lower_height(delta)
snow_height = lower_height - lower_margin

print(str(snow_height))


