import sys

weapons = [(4,8), (5,10), (6,25), (7,40), (8,74)]
armors = [(1,13), (2,31), (3,53), (4,75), (5,102)]
rings = [(1,0,25), (2,0,50), (3,0,100), (0,1,20), (0,2,40), (0,3,80)]

def getweapon():
    global weapons
    for w in weapons:
        yield w

def getarmor():
    yield None
    global armors
    for a in armors:
        yield a

def getrings():
    global rings
    yield None, None
    for i in xrange(len(rings)):
        yield None, rings[i]

    for i in xrange(len(rings)):
        for j in xrange(i+1, len(rings)):
            yield rings[i], rings[j]

def power(w, a, r1, r2):
    damage, cost = w
    damage += r1[0] if r1 is not None else 0
    damage += r2[0] if r2 is not None else 0
    armor = a[0] if a is not None else 0
    armor += r1[1] if r1 is not None else 0
    armor += r2[1] if r2 is not None else 0
    cost += a[1] if a is not None else 0
    cost += r1[2] if r1 is not None else 0
    cost += r2[2] if r2 is not None else 0
    return damage, armor, cost

def fight(damage, armor):
    hp = 100
    bhp = 109
    bd = 8
    ba = 2
    turn = True
    while hp > 0 and bhp > 0:
        if turn:
            bhp -= max(damage - ba, 1)
        else:
            hp -= max(bd - armor, 1)
        turn = not turn

    return hp > 0
 
maxcost = 0
for w in getweapon():
    for a in getarmor():
        for r1,r2 in getrings():
            dd, df, cost = power(w, a, r1, r2)        
            if not fight(dd, df):
                maxcost = max(maxcost, cost)

print(maxcost)
