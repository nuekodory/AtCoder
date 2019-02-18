import collections


points = []

for i in range(0, 3):
    p1, p2 = map(int, input().split(' '))
    points.extend([p1, p2])

counter = collections.Counter(points)
num_mode = counter.most_common(1)[0][1]
# print(num_mode)

if num_mode >= 3:
    print("NO")
else:
    print("YES")

exit(0)
