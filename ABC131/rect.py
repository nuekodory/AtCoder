def place(p_tuple):
    table.add(p_tuple)
    x, y = p_tuple
    ys = x_to_y[x]
    xs = y_to_x[y]

    if x in xs:
        xs.remove(x)
    if y in ys:
        ys.remove(y)

    # print(xs, ys)
    for x_i in xs:
        for y_i in ys:
            if (x_i, y_i) not in table:
                place((x_i, y_i))

    ys.add(y)
    xs.add(x)


num_plot = int(input())

plots_l = [tuple(map(int, input().split(' '))) for _ in range(0, num_plot)]
plots = set(sorted(plots_l))

table = set()
x_to_y = {i: set() for i in range(1, 10000)}
y_to_x = {i: set() for i in range(1, 10000)}

link_dict = {}

for plot in plots:
    if plot in table:
        continue
    place(plot)

for plot in plots:
    place(plot)

# print(table)
print(len(table) - len(plots))
