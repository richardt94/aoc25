#%%
with open("input4.txt", "r") as file:
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]
#%%
accessible = 0
q = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '@':
            neighbours = []
            if j > 0:
                neighbours.append(lines[i][j-1])
            if j < len(lines[i]) - 1:
                neighbours.append(lines[i][j+1])
            if i > 0:
                neighbours.append(lines[i-1][j])
                if j > 0:
                    neighbours.append(lines[i-1][j-1])
                if j < len(lines[i]) - 1:
                    neighbours.append(lines[i-1][j+1])
            if i < len(lines) - 1:
                neighbours.append(lines[i+1][j])
                if j > 0:
                    neighbours.append(lines[i+1][j-1])
                if j < len(lines[i]) - 1:
                    neighbours.append(lines[i+1][j+1])
            if sum(n == '@' or n == '$' for n in neighbours) < 4:
                accessible += 1
                lines[i][j] = '$'
                q.append((i, j))
# %%
print(accessible)
# %%
while q:
    i, j = q.pop(0)
    lines[i][j] = '#'
    neighbours = []
    if j > 0:
        neighbours.append((i, j-1))
    if j < len(lines[i]) - 1:
        neighbours.append((i, j+1))
    if i > 0:
        neighbours.append((i-1, j))
        if j > 0:
            neighbours.append((i-1, j-1))
        if j < len(lines[i]) - 1:
            neighbours.append((i-1, j+1))
    if i < len(lines) - 1:
        neighbours.append((i+1, j))
        if j > 0:
            neighbours.append((i+1, j-1))
        if j < len(lines[i]) - 1:
            neighbours.append((i+1, j+1))

    for ni, nj in neighbours:
        if lines[ni][nj] != '@':
            continue
        adjacent = []
        if nj > 0:
            adjacent.append(lines[ni][nj-1])
        if nj < len(lines[ni]) - 1:
            adjacent.append(lines[ni][nj+1])
        if ni > 0:
            adjacent.append(lines[ni-1][nj])
            if nj > 0:
                adjacent.append(lines[ni-1][nj-1])
            if nj < len(lines[ni]) - 1:
                adjacent.append(lines[ni-1][nj+1])
        if ni < len(lines) - 1:
            adjacent.append(lines[ni+1][nj])
            if nj > 0:
                adjacent.append(lines[ni+1][nj-1])
            if nj < len(lines[ni]) - 1:
                adjacent.append(lines[ni+1][nj+1])
        if sum(a == '@' or a == '$' for a in adjacent) < 4:
            q.append((ni, nj))
            lines[ni][nj] = '$'

# %%
print(sum(line.count('#') for line in lines))
# %%
