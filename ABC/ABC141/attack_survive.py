num_player, initial_point, num_quiz = map(int, input().split(' '))
answerer = [int(input()) for _ in range(0, num_quiz)]

points = [initial_point - num_quiz] * num_player

for i in answerer:
    points[i-1] += 1

survival = [point > 0 for point in points]

for b in survival:
    if b:
        print("Yes")
    else:
        print("No")

exit(0)
