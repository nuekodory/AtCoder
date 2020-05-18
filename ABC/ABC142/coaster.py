_, required_height = map(int, input().split(' '))

heights = list(map(int, input().split(' ')))
accepted = [h for h in heights if h >= required_height]

print(len(accepted))
exit(0)
