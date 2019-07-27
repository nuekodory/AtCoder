import collections


line = input().strip()

counter = collections.Counter(line)

if len(counter) == 2:
    former, latter = counter.most_common(2)
    if former[1] == latter[1] == 2:
        print("Yes")
        exit(0)

print("No")
exit(0)
