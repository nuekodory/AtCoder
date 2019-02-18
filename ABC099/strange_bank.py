input_num = int(input())

combinations = [(pow1, pow2, pow3, pow4, pow5, pow6)
                for pow1 in range(0, 6)
                for pow2 in range(0, 6)
                for pow3 in range(0, 6)
                for pow4 in range(0, 6)
                for pow5 in range(0, 6)
                for pow6 in range(0, 6)]

num_withdraw_list = []
for combination in combinations:
    pow1, pow2, pow3, pow4, pow5, pow6 = combination
    withdraw6 = 6 ** 1 * pow1 + 6 ** 2 * pow2 + \
                6 ** 3 * pow3 + 6 ** 4 * pow4 + \
                6 ** 5 * pow5 + 6 ** 6 * pow6

    if withdraw6 > input_num:
        continue
    else:
        rest = input_num - withdraw6
        num_withdraw = sum(combination)
        for i in reversed(range(1, 6)):
            withdraw_i = rest // 9 ** i
            rest -= 9 ** i * withdraw_i
            num_withdraw += withdraw_i
        num_withdraw += rest
        num_withdraw_list.append(num_withdraw)

print(str(min(num_withdraw_list)))
