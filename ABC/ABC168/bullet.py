from math import gcd
from collections import defaultdict


num_fish = int(input())
counter = defaultdict(int)
num_nonzero = 0
num_zero_pair = 0
num_one_zero_pair = 0

for i in range(0, num_fish):
    a, b = map(int, input().split(' '))

    if a == 0 and b == 0:
        num_zero_pair += 1
        continue
    elif a == 0 or b == 0:
        num_one_zero_pair += 1
        continue
    d = gcd(a, b)
    a = a // d
    b = b // d

    if a < 0:
        a = -a
        b = -b

    counter[(a, b)] += 1
    num_nonzero += 1

conflict = 0
for a, b in counter.keys():
    if b > 0:
        if (b, -a) in counter.keys():
            conflict += counter[(a, b)] * counter[(b, -a)]
    else:
        if (-b, a) in counter.keys():
            conflict += counter[(a, b)] * counter[(-b, a)]

conflict = conflict // 2
conflict += num_zero_pair * (num_nonzero + num_one_zero_pair)

print(counter)
print(conflict)
print(2 ** num_fish)






