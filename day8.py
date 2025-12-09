#%%
with open("input8.txt", "r") as file:
    lines = file.readlines()
    coords = [tuple(int(i) for i in l.split(',')) for l in lines]
# %%
dists = []
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        dist = (coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2 + (coords[i][2] - coords[j][2]) ** 2
        dists.append((dist, i, j))

circuits = [i for i in range(len(coords))]
# %%
for dist, i, j in sorted(dists)[:1000]:
    ci = circuits[i]
    cj = circuits[j]
    if ci != cj:
        for k in range(len(circuits)):
            if circuits[k] == cj:
                circuits[k] = ci


# %%
sizes = [0] * len(coords)

for ci in circuits:
    sizes[ci] += 1

# %%
ssize = sorted(sizes, reverse=True)
# %%
from math import prod
print(prod(ssize[:3]))

# %%

circuits = [i for i in range(len(coords))]
sdist = sorted(dists)
for dist, i, j in sdist:
    ci = circuits[i]
    cj = circuits[j]
    if ci != cj:
        for k in range(len(circuits)):
            if circuits[k] == cj:
                circuits[k] = ci
    if all(circuits[k] == circuits[0] for k in range(len(circuits))):
        break


# %%
x1, x2 = coords[i][0], coords[j][0]
print(x1 * x2)

# %%
