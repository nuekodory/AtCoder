import math


def combination(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)


reducer = 10**9 + 7
num_total, num_blue = map(int, input().split(' '))

num_red = num_total - num_blue
max_trial = min(num_blue, num_total - num_blue + 1)

for num_trial in range(1, max_trial+1):
    free_blue = num_blue - num_trial
    free_red = num_red - (num_trial - 1)

    blue_pot = num_trial
    red_pot = num_trial + 1

    pattern_red = combination(free_red + red_pot - 1, free_red)
    pattern_blue = combination(free_blue + blue_pot - 1, free_blue)

    print((pattern_red * pattern_blue) % reducer)

for _ in range(max_trial, num_blue):
    print("0")
