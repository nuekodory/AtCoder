num_candidate, thin_king = map(int, input().split(' '))

thin_candidates = [int(x) for x in input().split(' ')]
valid_candidates = [length for length in thin_candidates if length < thin_king]

if not valid_candidates:
    print(-1)
    exit(0)

valid_candidates.sort(reverse=True)
thin_partner = valid_candidates[0]
print(thin_candidates.index(thin_partner) + 1)
exit(0)
