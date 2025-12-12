
# %%
with open("input11.txt") as f:
    lines = f.readlines()
# %%
adj = {}
for line in lines:
    key, values = line.strip().split(':')
    adj[key] = values.strip().split(' ') if values else []
# %%
q = [('you', [])]
num_paths = 0
while q:
    node, path = q.pop(0)
    neighbours = adj[node]
    for neighbour in neighbours:
        if neighbour == 'out':
            num_paths += 1
        elif neighbour not in path:
            q.append((neighbour, path + [node]))
# %%
print(num_paths)
# %%
with open("test11-2.txt") as f:
    lines = f.readlines()

adj = {}
for line in lines:
    key, values = line.strip().split(':')
    adj[key] = values.strip().split(' ') if values else []
# %%
def paths(n_to, n_from):
    np_from = {n_to: 1}

    def count_paths(n):
        if n in np_from:
            return np_from[n]
        elif n not in adj:
            return 0
        total = 0
        for neighbour in adj[n]:
            total += count_paths(neighbour)
        np_from[n] = total
        return total

    return count_paths(n_from)

print(paths('out', 'you'))

# %%
print(paths('out', 'dac') * paths('dac', 'fft') * paths('fft', 'svr'))
print(paths('out', 'fft') * paths('fft', 'dac') * paths('dac', 'svr'))
# %%
