odds = ['R', 'U', 'D']
evens = ['L', 'U', 'D']

line = input().strip()

for i, c in enumerate(line):
    if (i+1) % 2 == 1:
        if c not in odds:
            print("No")
            exit(0)
    else:
        if c not in evens:
            print("No")
            exit(0)
else:
    print("Yes")
    exit(0)
