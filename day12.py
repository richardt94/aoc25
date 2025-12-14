# %%
import heapq, copy
# %%
with open("input12.txt") as f:
    data = f.read().strip()
# %%
shapes = []
areas = []
input_parts = data.split("\n\n")
for shape_str in input_parts[:-1]:
    shape = []
    shape_lines = shape_str.split("\n")[1:]
    area = 0
    for y, line in enumerate(shape_lines):
        for x, c in enumerate(line):
            if c == "#":
                shape.append((x, y))
                area += 1
    shapes.append(shape)
    areas.append(area)
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
unsolvable = 0
solvable = 0
for region in regions:
    region_area = region[0][0] * region[0][1]
    lb_area = sum(areas[i] * region[1][i] for i in range(len(shapes)))
    if region_area < lb_area:
        print("No solution for region", region)
        unsolvable += 1
        continue
    num_trivial_fits = (region[0][0] // 3) * (region[0][1] // 3)
    total_needed = sum(region[1])
    if num_trivial_fits >= total_needed:
        print("trivial solution for region", region)
        solvable += 1
        continue

    print("Unknown for region", region)
    print("trivial fit places:", num_trivial_fits, "total needed:", total_needed)

print("Solvable regions:", solvable)
    # print("Attempting search for region", region)

    # width = min(region[0][0], region[0][1])
    # height = max(region[0][0], region[0][1])

    # q = []

    # initial_board = [[0 for _ in range(height)] for _ in range(width)]

    # initial_state = (0, [0] * len(shapes), initial_board)

    # heapq.heappush(q, initial_state)

    # visited = set()

    # while q:
    #     current_height, shape_counts, board = heapq.heappop(q)
    #     if tuple(shape_counts) in visited:
    #         continue
    #     if shape_counts == list(region[1]):
    #         print("Found solution with height", current_height)
    #         solvable += 1
    #         break
    #     for (i, shape) in enumerate(shapes):
    #         w = max(x for x, y in shape) + 1
    #         for rot in range(4):
    #             for flip in [False, True]:
    #                 swap_xy = (rot % 2) == 1
    #                 invert_x = (rot == 2 or rot == 3)
    #                 invert_y = (rot == 1 or rot == 2)
    #                 invert_x = invert_x ^ flip
                    

    #                 for shape_bottom in range(min(current_height + 1, height - w + 1)):
    #                     for shape_left in range(width - w + 1):
    #                         new_board = copy.deepcopy(board)
    #                         touching = False
    #                         if all(b == 0 for b in shape_counts):
    #                             touching = True
    #                         for x, y in shape:
    #                             sx = x
    #                             sy = y
    #                             if invert_x:
    #                                 sx = w - 1 - sx
    #                             if invert_y:
    #                                 sy = w - 1 - sy
    #                             if swap_xy:
    #                                 sx, sy = sy, sx
    #                             board_x = shape_left + sx
    #                             board_y = shape_bottom + sy
    #                             if new_board[board_x][board_y] == 1:
    #                                 break
    #                             if board_x > 0:
    #                                 if new_board[board_x - 1][board_y] == 1:
    #                                     touching = True
    #                                 if board_y < height - 1:
    #                                     if new_board[board_x - 1][board_y + 1] == 1:
    #                                         touching = True
    #                                 if board_y > 0:
    #                                     if new_board[board_x - 1][board_y - 1] == 1:
    #                                         touching = True
    #                             if board_x < width - 1:
    #                                 if new_board[board_x + 1][board_y] == 1:
    #                                     touching = True
    #                                 if board_y < height - 1:
    #                                     if new_board[board_x + 1][board_y + 1] == 1:
    #                                         touching = True
    #                                 if board_y > 0:
    #                                     if new_board[board_x + 1][board_y - 1] == 1:
    #                                         touching = True
    #                             if board_y > 0:
    #                                 if new_board[board_x][board_y - 1] == 1:
    #                                     touching = True
    #                             if board_y < height - 1:
    #                                 if new_board[board_x][board_y + 1] == 1:
    #                                     touching = True
    #                             if not touching:
    #                                 break
                                
    #                         else:
    #                             for x, y in shape:
    #                                 sx = x
    #                                 sy = y
    #                                 if invert_x:
    #                                     sx = w - 1 - sx
    #                                 if invert_y:
    #                                     sy = w - 1 - sy
    #                                 if swap_xy:
    #                                     sx, sy = sy, sx
    #                                 board_x = shape_left + sx
    #                                 board_y = shape_bottom + sy
    #                                 new_board[board_x][board_y] = 1
    #                             new_shape_counts = copy.deepcopy(shape_counts)
    #                             new_shape_counts[i] += 1
    #                             new_height = max(current_height, shape_bottom + w)
    #                             new_state = (new_height, new_shape_counts, new_board)
    #                             heapq.heappush(q, new_state)
    #     visited.add(tuple(shape_counts))

    # else:
    #     print("No solution found")
    #     unsolvable += 1
                    
# %%
