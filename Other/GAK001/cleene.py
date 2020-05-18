import collections
from scipy.special import comb
# from scipy.misc import comb


if num_kind == 1:
    ans_external = 0
else:
    differ = [len(list(filter(arr[i].__gt__, arr))) for i in range(0, len_arr)]
    ans_external = sum(differ)

num_comb = comb(num_repeat, 2, exact=True)
ans = num_comb * ans_external + num_repeat * ans_internal
# print(f"inter: {ans_internal}, ext: {ans_external}, {num_comb} {num_repeat}")

print(ans % NUM_MOD)
exit(0)
