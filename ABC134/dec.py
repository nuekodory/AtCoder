len_arr = int(100000)

arr = [0] * 100000

current_min = {arr[-1]: 1}
current_max = arr[-1]
num_color = 1

for i in reversed(range(0, len_arr-1)):
    target = arr[i]

    if target >= current_max:
        num_color += 1
        current_min[target] = 1
        current_max = target
    else:
        acceptable = [x for x in current_min.keys() if x > target]
        selected = min(acceptable)

        if current_min[selected] == 1:
            del(current_min[selected])
            if target in current_min.keys():
                current_min[target] += 1
            else:
                current_min[target] = 1

        else:
            current_min[selected] -= 1

        current_max = max(target, current_max)

print(num_color)
exit(0)
