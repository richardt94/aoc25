with open("input1.txt") as f:
   instructions = f.readlines()

num_zeros = 0
passwd = 0
dial = 50
for instr in instructions:
   direction = -1 if instr[0] == "L" else +1
   distance = int(instr[1:])
   for _ in range(distance):
      dial += direction
      dial %= 100
      if dial == 0:
         passwd += 1
   if dial == 0:
      num_zeros += 1

print(num_zeros, passwd)
