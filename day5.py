# %%
with open("input5.txt") as file:
    ranges, ids = file.read().strip().split('\n\n')
    ranges = ranges.split('\n')
    ids = ids.split('\n')
# %%
range_set = set()
for r in ranges:
    low, high = [int(id) for id in r.split('-')]
    for low2, high2 in list(range_set):
        if low <= high2 + 1 and high >= low2 - 1:
            low = min(low, low2)
            high = max(high, high2)
            range_set.remove((low2, high2))
    range_set.add((low, high))
# %%
print(range_set)

# %%
fresh = 0
for id in ids:
    id = int(id)
    fresh += 1
    for low, high in range_set:
        if id >= low and id <= high:
            break
    else:
        fresh -= 1
# %%
print(fresh)

# %%
possible_fresh = 0
for low, high in range_set:
    possible_fresh += (high - low + 1)
# %%
print(possible_fresh)
# %%
