from collections import defaultdict


num_seq, num_charm = map(int, input().split(' '))
input_line = input()

koma_dict = defaultdict(list)
for index, char in enumerate(input_line):
    koma_dict[char].append(index+1)

count_koma_dict = {index: 1 for index in range(1, num_seq+1)}

for i in range(0, num_charm):
    target_char, destination = input().split(' ')
    targeted = koma_dict[target_char]

    for target in targeted:
        if destination == "R":
            if target == num_seq:
                count_koma_dict[target] = 0
            else:
                count_koma_dict[target+1] += count_koma_dict[target]
                count_koma_dict[target] = 0

        else:
            if target == 1:
                count_koma_dict[target] = 0
            else:
                count_koma_dict[target-1] += count_koma_dict[target]
                count_koma_dict[target] = 0

print(sum(count_koma_dict.values()))
exit(0)
