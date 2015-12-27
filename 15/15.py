import re
ings = list()
for line in open('input.txt'):
    m = re.compile('.*capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
    g = m.match(line)
    ings.append((int(g.group(1)), int(g.group(2)), int(g.group(3)), int(g.group(4)), int(g.group(5))))

def rate(s, m, f):
    pr = [s, m, f, 100-f-m-s]
    res = 1 
    global ings
    for i in xrange(4):
        s = 0
        for j, ing in enumerate(ings):
            s += ing[i]*pr[j]
        s = max(0, s)
        res *= s
    c = 0
    for j, ing in enumerate(ings):
        c += ing[4]*pr[j]

    return res if c == 500 else 0       
 
m = 0
for i in xrange(0, 101, 1):
    for j in xrange(0, 101-i, 1):
        for k in xrange(0, 101-j-i, 1):
            m = max(m, rate(i,j,k))

print(m)
               
