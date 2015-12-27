prev = list()
for line in open('input.txt'):
    prev.append([x for x in line.strip()])
def turncorners(state):
    print state[0]
    state[0] = ['#'] + state[0][1:99] + ['#']
    state[99] = ['#'] + state[99][1:99] + ['#']

def ison(x, y, state):
    ons = 0
    for i in xrange(x-1, x+2):
        for j in xrange(y-1, y+2):
            if (i,j) == (x,y):
                continue
            if i >=0 and i < 100 and j >= 0 and j < 100 and state[i][j] == '#':
                ons += 1

    return '#' if (state[x][y] == '#' and ons in (2,3) or state[x][y] == '.' and ons == 3) else '.'
        
turncorners(prev)
for i in xrange(100):
    nextt = [[ison(x,y,prev) for y in xrange(100)] for x in xrange(100)]
    turncorners(nextt)
    prev = nextt

total = 0
for i in xrange(100):
    total += nextt[i].count('#')

print(total)        
