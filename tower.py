<<<<<<< HEAD
def delta2lower_height(arg_num):
=======
def delta2height(arg_num):
>>>>>>> d352ca717d9b943f22ace9549b47fe80dcc11d7d
    height = 0
    for i in range(1, arg_num):
        height += i
    return height


input_line = input().split()

<<<<<<< HEAD
higher_margin = int(input_line[0])
lower_margin = int(input_line[1])

delta = higher_margin - lower_margin

lower_height = delta2lower_height(delta)
snow_height = lower_height - lower_margin
=======
west_margin = int(input_line[0])
east_margin = int(input_line[1])

delta = east_margin - west_margin

west_height = delta2height(delta)
snow_height = west_height - west_margin
>>>>>>> d352ca717d9b943f22ace9549b47fe80dcc11d7d

print(str(snow_height))


