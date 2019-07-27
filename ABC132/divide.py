num_test = int(input())

difficulties = [int(s) for s in input().split(' ')]

difficulties.sort()

center = num_test // 2
must_abc = difficulties[center-1]
must_arc = difficulties[center]

if must_abc == must_arc:
    print("0")
    exit(0)

print(must_arc - must_abc)
exit(0)
