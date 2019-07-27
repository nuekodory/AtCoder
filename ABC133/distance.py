import itertools
import math


num_point, dimension = map(int, input().split(' '))
points = {index: tuple(map(int, input().split(' '))) for index in range(0, num_point)}

trials = list(itertools.combinations(range(0, num_point), 2))

distances = [sum([(p1 - p2)**2 for p1, p2 in zip(points[trial[0]], points[trial[1]])]) for trial in trials]

ints = [distance for distance in distances if math.sqrt(distance) == int(math.sqrt(distance))]

print(len(ints))
