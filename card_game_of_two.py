num_cards = int(input())
input_line = input().split()

input_int = list(map(int, input_line))

input_int.sort(reverse=True)

score_alice = 0
score_bob = 0

for index, number in enumerate(input_int):
    if index % 2 == 0:
        score_alice += number
    else:
        score_bob += number

print(str(score_alice - score_bob))

