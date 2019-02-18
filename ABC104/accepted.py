input_line = input()

if input_line[0] != 'A' or input_line[0].islower():
    print("WA")
    exit()
if input_line[2:-1].count('C') != 1:
    print("WA")
    exit()

if input_line.count('A') == 1 and input_line.count('C') == 1:
    must_lower = input_line.replace('A', '').replace('C', '')
    if must_lower.islower():
        print("AC")
        exit()

print("WA")
exit()
