num_input = int(input())

restaurants = []
for index in range(1, num_input+1):
    name, score_str = input().split(' ')
    reduced_score = 100 - int(score_str)
    restaurants.append((name, reduced_score, index))

restaurants.sort()

ordered_indexes = [index for _, _, index in restaurants]

for index in ordered_indexes:
    print(index)

exit(0)
