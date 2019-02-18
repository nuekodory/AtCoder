_ = input()
input_line = input()

# main

numbers = [int(element) for element in input_line.split(' ')]

numbers.sort()

longest = numbers.pop()
sum_rest = sum(numbers)

if longest < sum_rest:
    print("Yes")
else:
    print("No")
