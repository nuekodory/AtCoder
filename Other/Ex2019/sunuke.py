from collections import defaultdict

num_seq, num_charm = map(int, input().split(' '))
input_line = input()

koma_dict = defaultdict(list)
for index, char in enumerate(input_line):
    koma_dict[index] = [char]

for i in range(0, num_charm):
    target_char, destination = input().split(' ')
    targeted = [index for index, characters in koma_dict.items() if target_char in characters]
    print(targeted)

    if destination == "L":
        for target in targeted:
            if target == 0:
                koma_dict[target] = []
            else:
                koma_dict[target-1].extend(koma_dict[target])
                koma_dict[target] = []
    else:
        for target in targeted:
            if target == num_seq-1:
                koma_dict[target] = []
            else:
                koma_dict[target+1].extend(koma_dict[target])
                koma_dict[target] = []
    print(koma_dict)

print(sum([len(value) for value in koma_dict.values()]))
exit(0)
