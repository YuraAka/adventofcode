def nxt(cur):
    return ((cur%33554393) * 252533) % 33554393

def diagiter(n):
    prev = None
    for i in xrange(n):
        currow = i
        for j in xrange(i+1):
            yield (currow, j), prev
            prev = (currow, j)
            currow -= 1        

def fill(n):
    mx = [[0 for i in xrange(n)] for j in xrange(n)]
    for cur, prev in diagiter(n):
        mx[cur[0]][cur[1]] = nxt(mx[prev[0]][prev[1]]) if prev else 20151125     

    print(mx[2980][3074])
fill(12000)
