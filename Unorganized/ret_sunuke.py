import matplotlib.pyplot as plt


def sunuke_sum(arg: str) -> int:
    sum_digit = 0
    for char in arg:
        sum_digit += int(char)
    return sum_digit


sunuke_list = []
for i in range(1, 2000):
    sunuke_list.append(i / sunuke_sum(str(i)))

plt.plot(sunuke_list)
plt.xlim(1001, 2000)
plt.ylim(0, 600)
plt.ylabel("number/sunuke(number)")
plt.show()
