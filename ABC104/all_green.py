import copy


def delete_by_index(arg_index: int, arg_list: list):
    for j, _, _, idx, _, _ in enumerate(arg_list):
        if idx == arg_index:
            arg_list.pop(j)
            return


input_line = input().split()

num_kind = int(input_line[0])
target_score = int(input_line[1])

cost_list = []

for i in range(1, num_kind+1):
    input_line = input().split()
    num_task = int(input_line[0])
    bonus = int(input_line[1])
    score = 100 * i

    if num_task == 1:
        cost_list.append((float(score + bonus), 1, i, 1, score + bonus))
    else:
        cost_list.append((float(score), 1, i, num_task - 1, score))
        cost_list.append((float(score + bonus / num_task), num_task, i, 1, score * num_task + bonus))

cost_list.sort(reverse=True)
cost_list_original = copy.deepcopy(cost_list)
print(cost_list)

# maximize estimated-score

current_score = 0
while current_score < target_score:
    _, num_max, index, , total = cost_list.pop()


