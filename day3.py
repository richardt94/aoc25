#%%
with open("input3.txt", "r") as file:
    batteries = file.readlines()
# %%
j = 0
for b in batteries:
    max_idx = 0
    max_digit = 0
    for (i, c) in enumerate(b.strip()):
        if int(c) > max_digit:
            max_digit = int(c)
            max_idx = i
    
    if max_idx == len(b.strip()) - 1:
        max1 = 0
        for (i, c) in enumerate(b.strip()[:max_idx]):
            if int(c) > max1:
                max1 = int(c)
        j += max1 * 10 + max_digit
    else:
        max2 = 0
        for (i, c) in enumerate(b.strip()[max_idx + 1 :]):
            if int(c) > max2:
                max2 = int(c)
        j += max_digit * 10 + max2
    
print(j)
# %%
j = 0
for b in batteries:
    tj = 0
    left = 0
    for digit in range(12):
        max_idx = 0
        max_digit = -1
        for (i, c) in enumerate(b.strip()[left:len(b.strip())-11+digit]):
            if int(c) > max_digit:
                max_digit = int(c)
                max_idx = i + left
        left = max_idx + 1
        tj = tj * 10 + max_digit
    j += tj
print(j)
# %%
