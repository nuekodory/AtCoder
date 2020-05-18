num_a, num_b = map(int, input().split(' '))

lesser = min(num_a, num_b)
greater = max(num_a, num_b)

distance = greater - lesser
if distance == 0:
    print(0)
elif distance % 2 == 0:
    print((lesser + greater) // 2)
else:
    print("IMPOSSIBLE")
exit(0)
