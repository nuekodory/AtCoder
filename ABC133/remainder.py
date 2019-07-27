import itertools


downer, upper = map(int, input().split(' '))

r_d = (downer // 2019) * 2019
u_d = (upper // 2019) * 2019

rng = range(downer, upper+1)

if r_d in rng or u_d in rng:
    print(0)
    exit(0)

numbers = set([min(i, abs(2019-i)) for i in rng])

c = itertools.combinations(numbers, 2)
s = [(i1 * i2) % 2019 for i1, i2 in c]
print(min(s))
