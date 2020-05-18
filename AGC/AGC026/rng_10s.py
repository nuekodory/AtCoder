num_example = int(input())

for _ in range(0, num_example):
    input_line = input().split()
    initial_lot, num_purchase, feed_line, feed = tuple(map(int, input_line))
    lots = [initial_lot]

    lot = initial_lot

    while True:
        # init
        # print(f"INIT: {lot}")
        available = lot - feed_line
        if available > num_purchase:
            purchase = available // num_purchase
        else:
            purchase = 1

        lot -= purchase * num_purchase

        # print(f"lot:{lot}")
        if lot < 0:
            print("No")
            break
        elif lot <= feed_line:
            # print(f"ADD: {feed}")
            lot += feed

        if lot in lots:
            print("Yes")
            break
        else:
            lots.append(lot)

