k, a, b = map(int, input().split(' '))

delta_per_act_hit = 1
delta_per_act_exchange = (b - a) / 2

if delta_per_act_hit >= delta_per_act_exchange:
    # no exchange; not worth to do
    print(1+k)
    exit(0)

else:
    # if there are sufficient number of biscuits, do exchanging
    num_exchangeable = (k - (a-1)) // 2

    if num_exchangeable <= 0:
        # no exchange; cannot do
        print(1+k)
        exit(0)
    else:
        # exchange as much as possible
        print(1 + (b-a) * num_exchangeable + (k - num_exchangeable*2))
        exit(0)
