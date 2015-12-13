import sys
import itertools

cities = list()
edges = list()

with open('input.txt') as input:
    for line in input:
        c, d = line.split('=')
        src, dst = c.split('to')
        src = src.strip()
        dst = dst.strip()
        d = -int(d.strip())
        if src not in cities:
            cities.append(src)
        if dst not in cities:
            cities.append(dst)

        edges.append((cities.index(src), cities.index(dst), d))
        edges.append((cities.index(dst), cities.index(src), d))

dist = [[sys.maxint for j in xrange(len(cities))] for i in xrange(len(cities))]
for edge in edges:
    dist[edge[0]][edge[1]] = edge[2]

mindist = sys.maxint

def length(path):
    result = 0
    global dist
    for i in xrange(1, len(path)):
        result += dist[path[i-1]][path[i]]
    #result += dist[path[-1]][path[0]]
    return result

def select(visited, v):
    global cities
    adj = [w for w in xrange(0, len(cities)) if dist[v][w] != sys.maxint and w not in visited]
    if len(visited) == len(cities):
        print(visited)
        curdist = length(visited)
        global mindist
        mindist = min(mindist, curdist)
        return

    for w in adj:
        if w not in visited:
            select(visited + [w], w)
        

#select([0], 0)

for path in itertools.permutations(xrange(len(cities))):
    mindist = min(mindist, length(path))

print(mindist)
        
