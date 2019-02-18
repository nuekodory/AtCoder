input_line = input().split()

num_array = int(input_line[0])
num_equal = int(input_line[1])

input_line = input()
array_str = input_line.split()

array = list(map(int, array_str))

for index, number in enumerate(array):
    if number == 1:
        index_min = index
        break

# from forward

equalized = 1
i = 1
while equalized < num_array:
    equalized += (num_equal - 1)
    # print(i, equalized)
    i += 1

print(i - 1)
