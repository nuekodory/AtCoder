input_num = int(input())

input_str = input().split()
input_int = list(map(int, input_str))

added = []
for index, number in enumerate(input_int):
    added.append(number + index + 1)

print(added)
mean = sum(added) / len(added)
delta = round(mean)

adjusted = []

for number in added:
    adjusted.append(abs(number - delta))
