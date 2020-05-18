import collections


MAX_DIGIT_BIN = 40


def xor(num_int1, num_int2):
    bin_str1 = format(num_int1, 'b')
    bin_str2 = format(num_int2, 'b')
    max_digit = max(len(bin_str1), len(bin_str2))

    bin_str1 = format(num_int1, '0{}b'.format(max_digit))
    bin_str2 = format(num_int2, '0{}b'.format(max_digit))

    xor_list = [bin_str1[-(digit+1)] != bin_str2[-(digit+1)] for digit in range(0, max_digit)]

    return sum([2**digit for digit in range(0, max_digit) if xor_list[digit]])


def int2bin(num):
    return format(num, '0{}b'.format(MAX_DIGIT_BIN))


# main

num_input, max_target = [int(elem) for elem in input().split(' ')]
numbers = [int(elem) for elem in input().split(' ')]
numbers.sort()
# print(numbers)

numbers_bin = list(map(int2bin, numbers))

proposal_num_str = ""

for position in range(-MAX_DIGIT_BIN, 0):
    sliced_num = [number_bin[position] for number_bin in numbers_bin]
    counter = collections.Counter(sliced_num)
    # print(counter)

    count_0 = counter['0']
    count_1 = counter['1']

    if count_0 > count_1:
        proposal_num_str = proposal_num_str + '1'
    else:
        proposal_num_str = proposal_num_str + '0'

# print(proposal_num_str)
proposal_num = int(proposal_num_str, base=2)

while proposal_num > max_target:
    # print("INVALID: ", proposal_num_str)
    proposal_num_str = proposal_num_str[1:]
    try:
        proposal_num = int(proposal_num_str, base=2)
    except ValueError:
        proposal_num = 0

else:
    # print("proposal:", proposal_num_str)
    # print([xor(proposal_num, num) for num in numbers])
    print(sum([xor(proposal_num, num) for num in numbers]))
    exit(0)
