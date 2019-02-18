input_line = input().split()

cake_a = int(input_line[0])
cake_b = int(input_line[1])

if cake_a > 8 or cake_b > 8:
    print(":(")
else:
    print("Yay!")
