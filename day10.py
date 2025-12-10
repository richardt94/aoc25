#%%
with open("test10.txt", "r") as file:
    problems = file.readlines()
# %%
target_states = []
move_sets = []
joltages = []
for problem in problems:
    moves = []
    tokens = problem.strip().split()
    for token in tokens:
        if token.startswith('['):
            target_state = tuple([1 * (c == '#') for c in token[1:-1]])
            target_states.append(target_state)
        elif token.startswith('('):
            moves.append(tuple(int(i) for i in token[1:-1].split(',')))
        elif token.startswith('{'):
            joltages.append(tuple(int(i) for i in token[1:-1].split(',')))
    move_sets.append(moves)


# %%
num_moves = []
for target_state, moves in zip(target_states, move_sets):
    state = tuple([0] * len(target_state))
    visited = set([state])
    q = [(state, 0)]

    while q:
        state, step = q.pop(0)
        if state == target_state:
            print(f"Solved in {step} steps")
            num_moves.append(step)
            break
        for move in moves:
            new_state = list(state)
            for i in move:
                new_state[i] = new_state[i] ^ 1
            new_state = tuple(new_state)
            if new_state not in visited:
                q.append((new_state, step + 1))
                visited.add(new_state)

# %%
print(sum(num_moves))


# %%
import numpy as np
from scipy.optimize import linprog

num_moves = []
for target_state, moves in zip(joltages, move_sets):
    b = np.array(target_state)
    A = np.zeros((len(b), len(moves)), dtype=int)
    for j, move in enumerate(moves):
        for i in move:
            A[i, j] = 1
    
    move_soln = linprog(c=np.ones(len(moves)), A_eq=A, b_eq=b, integrality=np.ones(len(moves))).x
    move_soln = np.round(move_soln).astype(int)
    num_moves.append(np.sum(move_soln))
#%%
print(sum(num_moves))
# %%
