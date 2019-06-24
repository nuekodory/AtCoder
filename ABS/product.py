def digit_sum(number):
    s = str(number)
    sum_digit = 0
    for c in s:
        sum_digit += int(c)

    return sum_digit


if __name__ == "__main__":
    n, a, b = map(int, input().split(' '))
    success = 0
    for i in range(1, n+1):
        if a <= digit_sum(i) <= b:
            success += i

    print(success)
    exit(0)
