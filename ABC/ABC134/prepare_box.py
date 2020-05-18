len_arr = int(input())

conditions = [int(x) for x in input().split(' ')]
arr = [None] * len_arr

for i in reversed(range(0, len_arr)):
    sliced_arr = arr[i::i+1]
    current_condition = sum(sliced_arr[1:]) % 2

    if current_condition == conditions[i]:
        arr[i] = 0
    else:
        arr[i] = 1

# print(arr)
ball_indexes = [j+1 for j, ball in enumerate(arr) if ball == 1]

len_ans = len(ball_indexes)
print(len_ans)

if len_ans != 0:
    print(' '.join(map(str, ball_indexes)))

exit(0)
