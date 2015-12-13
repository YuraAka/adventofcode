import re

lights = [[0 for y in xrange(0, 1000)] for x in xrange(0, 1000)]
ons = 0

def on(x, y):
    if True or lights[x][y] == False:
        lights[x][y] += 1
        global ons
        ons += 1

def off(x, y):
    if lights[x][y] > 0:
        lights[x][y] -= 1
        global ons
        ons -= 1

def toggle(x, y):
    '''
    if lights[x][y] == True:
        off(x,y)
    else:
        on(x,y)
    '''
    on(x,y)
    on(x,y)
    

def turn(sx, sy, fx, fy, action):
    for x in xrange(sx, fx+1):
        for y in xrange(sy, fy+1):
            action(x, y)
    

def parse(line):
    m = re.search('.* (\d+,\d+) through (\d+,\d+)', line.strip())
    action = on if line.startswith('turn on') else off if line.startswith('turn off') else toggle
    return action, m.group(1).split(','), m.group(2).split(',')

with open('input.txt') as input:
    for line in input:
        action, start, finish = parse(line)
        turn(int(start[0]), int(start[1]), int(finish[0]), int(finish[1]), action)

print(ons)
            
