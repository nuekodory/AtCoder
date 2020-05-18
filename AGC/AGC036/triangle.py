# calc
seq = {i: 10 ** i for i in range(0, 9+1)}
squared = {index: x ** 2 for index, x in seq.items()}


def sq(number):
    for i, s in squared.items():
        if number <= s:
            return i


def main():
    target = int(input())
    first_e = sq(target)
    first = 10 ** first_e

    if target == squared[first_e]:
        second = first
    else:
        second = (target // seq[first_e]) + 1
    over = first * second
    rest = over - target
    x0 = 0
    y0 = 0
    x1 = first
    y1 = 1
    x2 = rest
    y2 = second
    print(x0, y0, x1, y1, x2, y2)


if __name__ == '__main__':
    main()



