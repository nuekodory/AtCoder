input_line = input()

index = 0
while index < len(input_line):
    str_five = input_line[index:index+5]
    if str_five == "dream":
        if index+5 == len(input_line):
            print("YES")
            exit(0)
        try:
            if input_line[index+5:index+7] == "er":
                if index+7 == len(input_line):
                    print("YES")
                    exit(0)
                elif input_line[index+5:index+10] == "erase":
                    index += 5
                    continue
                else:
                    index += 7
                    continue
            else:
                index += 5

        except IndexError:
            print("NO")
            exit(0)
    elif str_five == "erase":
        if index+5 == len(input_line):
            print("YES")
            exit(0)
        try:
            if input_line[index+5:index+6] == "r":
                if index+6 == len(input_line):
                    print("YES")
                    exit(0)
                else:
                    index += 6
                    continue
            else:
                index += 5
        except IndexError:
            print("NO")
            exit(0)
    else:
        print("NO")
        exit(0)
else:
    print("NO")
    exit(0)
