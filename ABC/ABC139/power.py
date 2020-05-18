import math


socket_on_tap, target = map(int, input().split(' '))

print(math.ceil((target - 1) / (socket_on_tap - 1)))
exit(0)
