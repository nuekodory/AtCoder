string = input().strip()

is_r = [c == 'R' for c in string]

cond = [1] * len(is_r)
cond_list = []

for i in range(0, 10**100):
    new_cond = [0] * len(is_r)
    for d in range(0, len(is_r)):
        if is_r[d]:
            new_cond[d+1] += cond[d]
        else:
            new_cond[d-1] += cond[d]
    print(i, new_cond)
    if new_cond in cond_list:
        print("looping")
        exit(0)
    cond = new_cond
    cond_list.append(cond)
