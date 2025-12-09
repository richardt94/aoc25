#%%
with open("input7.txt") as file:
    data = [line.strip() for line in file.readlines()]
#%%
x = set()
for i, ch in enumerate(data[0]):
    if ch == 'S':
        x.add(i)
# %%
splits = 0
for line in data[1:]:
    new_x = x.copy()
    for i, ch in enumerate(line):
        if ch == '^':
            if i in x:
                new_x.add(i - 1)
                new_x.add(i + 1)
                new_x.remove(i)
                splits += 1
    x = new_x



# %%
print(splits, x)
# %%
x = {}
for i, ch in enumerate(data[0]):
    if ch == 'S':
        x[i] = 1
# %%
for line in data[1:]:
    new_x = {}
    for i in x:
        if line[i] == '^':
            new_x[i - 1] = new_x.get(i - 1, 0) + x[i]
            new_x[i + 1] = new_x.get(i + 1, 0) + x[i]
        else:
            new_x[i] = new_x.get(i, 0) + x[i]
    x = new_x

# %%
print(sum(x.values()), x)
# %%
