def exec_ncr(max_step, record_dict):
    for i in range(2, max_step+1):
        record_dict[i] = record_dict[i-1] + record_dict[i-2]


num_stair, num_wet = map(int, input().split(' '))

last_wet = -1
num_pattern = 1
d = {0: 1, 1: 1}
exec_ncr(num_stair, d)

for i in range(0, num_wet):
    wet = int(input())
    dry_step = wet - last_wet - 1
    last_wet = wet

    if dry_step <= 0:
        print('0')
        exit(0)

    elif dry_step == 1 or dry_step == 2:
        continue

    else:
        num_pattern *= d[dry_step-1]

# last step
dry_step = num_stair - last_wet

num_pattern *= d[dry_step-1]

print(num_pattern % 1000000007)
exit(0)
