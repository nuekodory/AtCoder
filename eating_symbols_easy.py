orders = input()

number = 0
for order in orders:
    if order == '+':
        number += 1
    else:    # order == '-'
        number -= 1

print(str(number))