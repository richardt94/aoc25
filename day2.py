#%%
with open("test2.txt", "r") as file:
    ranges = [r.strip() for r in file.read().split(",")]
# %%
with open("input2.txt", "r") as file:
    ranges = [r.strip() for r in file.read().split(",")]
# %%
total = 0
for r in ranges:
    rmin, rmax = [int(i) for i in r.split("-")]
    for i in range(rmin, rmax + 1):
        strrep = str(i)
        if strrep[:len(strrep)//2] == strrep[len(strrep)//2:]:
            print(i)
            total += i
# %%
print("Total:", total)
# %%
total = 0
for r in ranges:
    rmin, rmax = [int(i) for i in r.split("-")]
    for i in range(rmin, rmax + 1):
        strrep = str(i)
        for num_reps in range(2, len(strrep) + 1):
            if len(strrep) % num_reps != 0:
                continue
            rep_length = len(strrep)//num_reps
            if all(
                strrep[j*rep_length:(j+1)*rep_length] == strrep[0:rep_length]
                for j in range(1, num_reps)
            ):
                print(i)
                print(num_reps)
                total += i
                break
# %%
print("Total:", total)
# %%
