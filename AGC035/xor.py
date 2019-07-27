from collections import Counter


num_hat = int(input())

numbers = [int(i) for i in input().split(' ')]
counter = Counter(numbers)

print(max(counter))
