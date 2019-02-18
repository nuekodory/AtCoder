input_num = int(input())

max_withdraw = 100000
current_withdraw = input_num
# greedy 9max=5 6max=7 1max=100000

count = 0
for i in reversed(range(1, 6)):
    for j in reversed(range(1, 9)):
        if (9 ** i) * j <= current_withdraw:
            print("withdraw {} times: {}".format(9 ** i, j))
            count += j
            current_withdraw -= (9 ** i) * j

for i in reversed(range(1, 8)):
    for j in reversed(range(1, 6)):
        if (6 ** i) * j <= current_withdraw:
            print("withdraw {} times: {}".format(6 ** i, j))
            count += j
            current_withdraw -= (6 ** i) * j

count += current_withdraw
max_withdraw = count

print(str(max_withdraw))

current_withdraw = input_num



