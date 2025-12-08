#%%
with open("input6.txt") as file:
    data = file.read().strip().split('\n')
    data = [l.split() for l in data]
# %%
data
# %%
grand_total = 0
for problem_i in range(len(data[0])):
    op = data[-1][problem_i]
    args = []
    for row in data[:-1]:
        args.append(int(row[problem_i]))

    if op == '+':
        grand_total += sum(args)
    elif op == '*':
        total = 1
        for a in args:
            total *= a
        grand_total += total
#%%
print(grand_total)
# %%
with open("input6.txt") as file:
    data = file.read().strip('\n').split('\n')
#%%
grand_total = 0
args = []
for col in range(len(data[-1])-1, -1, -1):
    if all(data[row][col] == ' ' for row in range(len(data)-1)):
        continue
    num = int(''.join(data[row][col] for row in range(len(data)-1)).strip())
    args.append(num)
    if data[-1][col] in '+*':
        op = data[-1][col]
        if op == '+':
            grand_total += sum(args)
        elif op == '*':
            total = 1
            for a in args:
                total *= a
            grand_total += total
        args = []        

# %%
print(grand_total)

# %%
