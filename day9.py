#%%
from itertools import combinations
#%%
with open("input9.txt", "r") as file:
    lines = file.readlines()

points = [tuple(int(i) for i in l.strip().split(',')) for l in lines]
#%%

max_area = 0
for (x1, y1), (x2, y2) in combinations(points, 2):
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    if area > max_area:
        max_area = area

print(max_area)


# %%
xp, yp = points[0][0], points[0][1]
lines = []
for x, y in points[1:]:
    lines.append([(xp, yp), (x, y)])
    xp, yp = x, y
lines.append([(xp, yp), points[0]])

# %%
max_area = 0
for (x1, y1), (x2, y2) in combinations(points, 2):
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    if area > max_area:
        max_area = area

print(max_area)
# %%
import matplotlib.pyplot as plt

for line in lines:
    x_values = [line[0][0], line[1][0]]
    y_values = [line[0][1], line[1][1]]
    plt.plot(x_values, y_values, marker='x', color='k', markersize=3)
# %%
max_area = 0
max_UL = None
max_LR = None
for (x1, y1), (x2, y2) in combinations(points, 2):
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    x_ul, y_ul = min(x1, x2), min(y1, y2)
    x_lr, y_lr = max(x1, x2), max(y1, y2)

    for (x1, y1), (x2, y2) in lines:
        # horizontal collision
        collision_low = y_ul
        collision_high = y_lr
        # deal with anticlockwise perimeter - collide a line
        # with the 'left' edge of the box (from the line perspective)
        if x1 < x2:
            collision_high += 1
        else:
            collision_low -= 1
        if y1 == y2 and collision_low < y1 and y1 < collision_high:
            x1_intersect = max(x_ul, x1)
            x1_intersect = min(x_lr, x1_intersect)
            x2_intersect = max(x_ul, x2)
            x2_intersect = min(x_lr, x2_intersect)
            if abs(x1_intersect - x2_intersect) > 0:
                break
        # vertical collision
        collision_low = x_ul
        collision_high = x_lr
        if y1 < y2:
            collision_low -= 1
        else:
            collision_high += 1
        if x1 == x2 and collision_low < x1 and x1 < collision_high:
            y1_intersect = max(y_ul, y1)
            y1_intersect = min(y_lr, y1_intersect)
            y2_intersect = max(y_ul, y2)
            y2_intersect = min(y_lr, y2_intersect)
            if abs(y1_intersect - y2_intersect) > 0:
                break
    else:
        if area > max_area:
            max_area = area
            max_UL = (x_ul, y_ul)
            max_LR = (x_lr, y_lr)

print(max_area, max_UL, max_LR)


# %%
(x1, y1), (x2, y2) = max_UL, max_LR
for line in lines:
    x_values = [line[0][0], line[1][0]]
    y_values = [line[0][1], line[1][1]]
    plt.plot(x_values, y_values, marker='x', color='k', markersize=3)

plt.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], color='r')
plt.show()
# %%
