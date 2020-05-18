d_jump = int(input())
goal_x, goal_y = map(int, input().split(' '))

d_goal = abs(goal_x) + abs(goal_y)

is_even_jump = d_jump % 2 == 0
is_even_goal = d_goal % 2 == 0

if is_even_jump and not is_even_goal:
    print(-1)
    exit(0)

if d_goal == d_jump:
    print(1)
    print(goal_x, goal_y)
    exit(0)

num_move = 0
d = d_goal
x = 0
y = 0