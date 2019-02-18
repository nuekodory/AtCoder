input_line = input().split()
total_cake = int(input_line[0])
select_cake = int(input_line[1])

cake_scores = []

for i in range(0, total_cake):
    input_line = input().split()
    beauty = int(input_line[0])
    yummy = int(input_line[1])
    common = int(input_line[2])

    cake_scores.append((beauty, yummy, common))

# + beauty + yummy + common score_p_p_p
# + beauty + yummy - common score_p_p_n
# + beauty - yummy + common score_p_n_p
# - beauty + yummy + common score_n_p_p
# - beauty - yummy + common score_n_n_p
# + beauty - yummy - common score_p_n_n
# - beauty + yummy - common score_n_p_n
# - beauty - yummy - common score_n_n_n

scores_p_p_p = []
scores_p_p_n = []
scores_p_n_p = []
scores_n_p_p = []
scores_n_n_p = []
scores_p_n_n = []
scores_n_p_n = []
scores_n_n_n = []

for i in range(0, total_cake):
    beauty, yummy, common = cake_scores[i]
    scores_p_p_p.append(beauty + yummy + common)
    scores_p_p_n.append(beauty + yummy - common)
    scores_p_n_p.append(beauty - yummy + common)
    scores_n_p_p.append(-beauty + yummy + common)
    scores_n_n_p.append(-beauty - yummy + common)
    scores_p_n_n.append(beauty - yummy - common)
    scores_n_p_n.append(-beauty + yummy - common)
    scores_n_n_n.append(-beauty - yummy - common)

scores_p_p_p.sort(reverse=True)
scores_p_p_n.sort(reverse=True)
scores_p_n_p.sort(reverse=True)
scores_n_p_p.sort(reverse=True)
scores_n_n_p.sort(reverse=True)
scores_p_n_n.sort(reverse=True)
scores_n_p_n.sort(reverse=True)
scores_n_n_n.sort(reverse=True)

score_p_p_p = sum(scores_p_p_p[0:select_cake])
score_p_p_n = sum(scores_p_p_n[0:select_cake])
score_p_n_p = sum(scores_p_n_p[0:select_cake])
score_n_p_p = sum(scores_n_p_p[0:select_cake])
score_n_n_p = sum(scores_n_n_p[0:select_cake])
score_p_n_n = sum(scores_p_n_n[0:select_cake])
score_n_p_n = sum(scores_n_p_n[0:select_cake])
score_n_n_n = sum(scores_n_n_n[0:select_cake])

print(str(max(score_p_p_p, score_p_p_n, score_p_n_p, score_n_p_p, score_n_n_p, score_p_n_n, score_n_p_n, score_n_n_n)))

