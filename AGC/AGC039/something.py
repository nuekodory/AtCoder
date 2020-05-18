MOD = 998244353


def dig(pos, depth, visited, graph):
    dest = graph[pos]
    if dest == pos:
        arr[pos] = 0
        arr[dest] = 0
    elif dest in visited.keys():
        res = depth - visited[dest] + 1
        for v in visited.keys():
            if visited[v] >= visited[dest]:
                arr[v] = res
    else:
        visited[dest] = depth+1
        dig(dest, depth+1, visited, graph)


num_pow = int(input())
range_upper = int(input(), base=2)

const = pow(2, num_pow-1)
calc_upper = max(pow(2, num_pow), range_upper)

arr = [None] * (calc_upper+1)
graph_dict = {i: i//2 + const*((i+1) % 2) for i in range(0, calc_upper+1)}

for i in range(0, range_upper+1):
    if arr[i] is not None:
        continue
    else:
        arr[i] = 0
        dig(i, 0, {i: 0}, graph_dict)

# print(list(graph_dict.items())[:40])
# print(arr[:2000])
print(sum([x for x in arr[:range_upper+1] if x is not None]) % MOD)


