# %%
import heapq, copy
# %%
with open("test12.txt") as f:
    data = f.read().strip()
# %%
shapes = []
input_parts = data.split("\n\n")
for shape_str in input_parts[:-1]:
    shape = []
    shape_lines = shape_str.split("\n")[1:]
    for y, line in enumerate(shape_lines):
        for x, c in enumerate(line):
            if c == "#":
                shape.append((x, y))
    shapes.append(shape)
# %%

regions = []
region_strs = input_parts[-1].split("\n")
for region_str in region_strs:
    region = []
    region_tokens = region_str.split(" ")
    region_size = region_tokens[0].strip(':').split('x')
    region_size = tuple(int(s) for s in region_size)
    region_target = tuple(int(c) for c in region_tokens[1:])
    regions.append((region_size, region_target))
# %%
region = regions[0]

width = min(region[0][0], region[0][1])
height = max(region[0][0], region[0][1])

q = []

initial_board = [[0] * height] * width

initial_state = (0, [0 * len(shapes)], initial_board)

heapq.heappush(q, initial_state)

while q:
    current_height, shape_counts, board = heapq.heappop(q)
    print(board)
    if shape_counts == list(region[1]):
        print("Found solution with height", current_height)
        break
    for (i, shape) in enumerate(shapes):
        w = max(x for x, y in shape) + 1
        h = max(y for x, y in shape) + 1
        for rot in range(4):
            for flip in [False, True]:
                swap_xy = (rot % 2) == 1
                invert_x = (rot == 2 or rot == 3)
                invert_y = (rot == 1 or rot == 2)
                invert_x = invert_x ^ flip
                

                for shape_bottom in range(current_height + 1):
                    for shape_left in range(width - sw + 1):
                        new_board = copy.deepcopy(board)
                        can_place = True
                        for x, y in shape:
                            print(sx, sy)
                            sx = x
                            sy = y
                            if invert_x:
                                sx = sw - 1 - sx
                            if invert_y:
                                sy = sh - 1 - sy
                            if swap_xy:
                                sx, sy = sy, sx
                            board_x = shape_left + sx
                            board_y = shape_bottom + sy
                            if new_board[board_x][board_y] == 1:
                                break
                            new_board[board_x][board_y] = 1
                        else:
                            new_shape_counts = copy.deepcopy(shape_counts)
                            new_shape_counts[i] += 1
                            new_height = max(current_height, shape_bottom + sh)
                            new_state = (new_height, new_shape_counts, new_board)
                            heapq.heappush(q, new_state)
                



# %%
