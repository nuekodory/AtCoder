len_arr = int(input())

arr = [int(input()) for _ in range(0, len_arr)]

current_min = {arr[-1]: 1}
num_color = 1

for i in reversed(range(0, len_arr-1)):
    target = arr[i]
    current_set = current_min.keys()
    # print(current_min)
    m = max(current_set)

    if target >= m:
        num_color += 1
        if target == m:
            current_min[target] += 1
        else:
            current_min[target] = 1
    else:
        acceptable = [x for x in current_set if x > target]
        # print(acceptable)
        selected = min(acceptable)

        if current_min[selected] == 1:
            del(current_min[selected])
            if target in current_set:
                current_min[target] += 1
            else:
                current_min[target] = 1

        else:
            current_min[selected] -= 1

print(num_color)
exit(0)
