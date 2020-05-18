array_length = int(input())
input_line = input().split()

array_int = list(map(int, input_line))
array_bin = list(map(bin, array_int))
array_bin_str = list(map(str, array_bin))

array_dividable = []

for i in range(0, array_length):
    if array_int[i] == 0:
        array_dividable.append(0)
    else:
        target_line = array_bin_str[i]
        count_dividable = 0
        for j in range(1, len(target_line)):
            target_char = target_line[-j]
            if target_char == '1':
                break
            elif target_char == 'b':
                break
            else:
                count_dividable += 1

        array_dividable.append(count_dividable)

if sum(array_dividable) == 0:
    print("0")
else:
    print(str(sum(array_dividable)))

