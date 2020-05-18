input_line = input().split()
num_bills = int(input_line[0])
sum_bills = int(input_line[1])

for num_10000 in reversed(range(0, num_bills + 1)):
    num_bills_rest = num_bills - num_10000
    for num_5000 in range(0, num_bills_rest + 1):
        num_1000 = num_bills_rest - num_5000
        if num_10000 * 10000 + num_5000 * 5000 + num_1000 * 1000 == sum_bills:
            print("{} {} {}".format(num_10000, num_5000, num_1000))
            exit(0)

else:
    print("-1 -1 -1")
