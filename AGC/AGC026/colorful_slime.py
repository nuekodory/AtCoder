num_slimes = int(input())
input_line = input().split()

slimes = list(map(int, input_line))

emerged_slimes = []

past_color = slimes[0]
block = 0

for color in slimes:
    if past_color == color:
        block += 1
    else:
        emerged_slimes.append(block)
        past_color = color
        block = 1
else:
    emerged_slimes.append(block)

summon = 0
for element in emerged_slimes:
    if element > 1:
        summon += element // 2

print(str(summon))
