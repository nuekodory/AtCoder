num_str = input().strip()
number = int(num_str)

if len(num_str) == 1:
    print(number)
elif len(num_str) == 2:
    print(9)
elif len(num_str) == 3:
    print(number - 100 + 1 + 9)
elif len(num_str) == 4:
    print(909)
elif len(num_str) == 5:
    print(number - 10000 + 1 + 900 + 9)
elif len(num_str) == 6:
    print(90909)
exit(0)
