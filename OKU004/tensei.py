str_count, str_converted_count = input().split(' ')
count = int(str_count)

for i in reversed(range(2, 10+1)):
    count_candidate = int(str_converted_count, base=i)
    if count_candidate == count:
        print(i)
        exit(0)
