import itertools
import re

with open('input.txt') as input:
    names = list()
    dist = dict()
    m = re.compile('(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).*')
    for line in input:
        res = m.match(line)
        src = res.group(1)
        op = res.group(2)
        value = res.group(3)
        dst = res.group(4)

        if src not in names:
            names.append(src)
        if dst not in names:
            names.append(dst)
        if 'me' not in names:
            names.append('me')

        src = names.index(src)
        dst = names.index(dst)
        me = names.index('me')
        value = int(value) if op == 'gain' else -int(value)
        if src not in dist:
            dist[src] = dict()
        if me not in dist:
            dist[me] = dict()

        dist[src][dst] = value
        dist[src][me] = 0
        dist[me][src] = 0
       
    result = 0
    for path in itertools.permutations(xrange(len(names))):
        total = 0
        for i in xrange(1, len(path)):
            total += dist[path[i-1]][path[i]] + dist[path[i]][path[i-1]]
        total += dist[path[0]][path[len(path)-1]] + dist[path[len(path)-1]][path[0]]
        result = max(result, total)

    print(result)
