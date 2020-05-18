def distance_to_right(p, point_list):
    if p == len(point_list) - 1:
        return None
    else:
        return point_list[p+1] - point_list[p]


# main

num_koma, num_to_visit = [int(element) for element in input().split(' ')]
points = [int(element) for element in input().split(' ')]

points.sort()

costs = [distance_to_right(p, points) for p in range(0, num_to_visit-1)]
costs.sort()

if num_koma == 1:
    print(sum(costs))
else:
    print(sum(costs[:-(num_koma-1)]))
