from collections import Counter


repeated = input().strip()
num_repeat = int(input())

len_repeated = len(repeated)

if len_repeated == 1:
    print(num_repeat // 2)

elif len_repeated == 2:
    if repeated[0] == repeated[1]:
        print(num_repeat)
    else:
        print(0)

else:
    c = Counter(repeated)
    # characters are all same, like aaa
    if len(c) == 1:
        print((num_repeat * len_repeated) // 2)
    #
    else:
        arr = [1]
        for i in range(1, len_repeated):
            if repeated[i - 1] == repeated[i]:
                arr[-1] += 1
            else:
                arr.append(1)

        if repeated[0] == repeated[-1]:
            change_first = sum([i//2 for i in arr[:-1]])
            change_last = arr[-1] // 2
            elem = arr.pop(0) + arr.pop(-1)
            arr.append(elem)
            change_rep = sum([i//2 for i in arr])
            print(change_first + change_rep * (num_repeat-1) + change_last)

        else:
            print(sum([i//2 for i in arr]) * num_repeat)

exit(0)
