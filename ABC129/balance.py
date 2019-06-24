num_weight = int(input())

weights = list(map(int, input().split(' ')))

deltas = []
total = sum(weights)

for i in range(1, num_weight):
    s1 = sum(weights[:i])
    s2 = total - s1
    delta = abs(s1 - s2)
    deltas.append(delta)

print(min(deltas))
exit(0)
