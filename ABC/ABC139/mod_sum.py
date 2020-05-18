def stair_sum(x):
    return (x * (x+1)) // 2


target = int(input())

print(stair_sum(target-1))
