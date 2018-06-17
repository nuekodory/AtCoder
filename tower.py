def delta2height(arg_num):
    height = 0
    for i in range(1, arg_num):
        height += i
    return height


input_line = input().split()

west_margin = int(input_line[0])
east_margin = int(input_line[1])

delta = east_margin - west_margin

west_height = delta2height(delta)
snow_height = west_height - west_margin

print(str(snow_height))


