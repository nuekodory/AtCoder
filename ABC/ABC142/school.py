num_student = int(input())
attend_list = [(x, i+1) for i, x in enumerate(list(map(int, input().split(' '))))]
attend_list.sort()

print(' '.join(map(str, [tup[1] for tup in attend_list])))
exit(0)
