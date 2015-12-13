def step(cmd, pos):
    if cmd == '^':
        return pos[0], pos[1]+1
    if cmd == '<':
        return pos[0]-1, pos[1]
    if cmd == '>':
        return pos[0]+1, pos[1]
    if cmd == 'v':
        return pos[0], pos[1]-1

houses = set()
houses.add((0,0))
with open('input.txt') as input:
    cur = (0,0)
    cur2 = (0,0)
    cmds = input.readline().strip()
    for i, cmd in enumerate(cmds):
        if i % 2:
            cur = step(cmd, cur)
            houses.add(cur)
        else:
            cur2 = step(cmd, cur2)
            houses.add(cur2)

print(houses)
print(len(houses))
