cmds = open('input.txt').readline()
floor = 0
cmds = cmds.strip()
pos = 0
for cmd in cmds:
    floor += 1 if cmd == '(' else -1
    pos += 1
    if floor == -1:
        print(pos)

print(floor)
