def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return set(divisors)


def is_dividable(x, d_set):
    for d in d_set:
        if x % d == 0 and d != 1:
            return True

    return False


a, b = map(int, input().split(' '))
divs_a = make_divisors(a)
divs_b = make_divisors(b)

common_div = [x for x in divs_a if x in divs_b]
common_div.sort()

seq = set()
for x in common_div:
    if not is_dividable(x, seq):
        seq.add(x)

# print(seq)
print(len(seq))
