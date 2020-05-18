input_line = input().split()

a = int(input_line[0])
b = int(input_line[1])

if a + b == 15:
    print("+")
elif a * b == 15:
    print("*")
else:
    print("x")
