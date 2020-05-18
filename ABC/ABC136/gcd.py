def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors


len_arr, max_move = map(int, input().split(' '))
arr = [int(x) for x in input().split(' ')]

sum_arr = sum(arr)
trials = make_divisors(sum_arr)
for t in trials:
    div_arr = [i % t for i in arr]
    if sum(div_arr) % t == 0:
        div_arr
    else:
        continue
