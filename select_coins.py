max_num_500yen = int(input())
max_num_100yen = int(input())
max_num_50yen = int(input())
total_cash = int(input())

patterns = []
correct_patterns = []

for i in range(0, max_num_500yen+1):
    for j in range(0, max_num_100yen+1):
        for k in range(0, max_num_50yen+1):
            patterns.append((i, j, k))

for pattern in patterns:
    num_500yen, num_100yen, num_50yen = pattern
    current_cash = 500 * num_500yen + 100 * num_100yen + 50 * num_50yen
    if current_cash == total_cash:
        correct_patterns.append(pattern)

print(len(correct_patterns))

