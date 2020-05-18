import math


num_tree, watchable_diff = map(int, input().split(' '))

per_watcher = watchable_diff * 2 + 1

print(math.ceil(num_tree / per_watcher))
exit(0)
