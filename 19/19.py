import heapq

rules = []
molecula = str()
with open('input.txt') as input:
    for line in input:
        if line == '\n':
            break
        k, v = line.strip().split(' => ')
        rules.append((k,v))

    for line in input:
        molecula = line.strip()

def expand(mol):
    for rule in rules:
        for i in xrange(len(mol)-len(rule[0])+1):
            if mol[i:i+len(rule[0])] == rule[0]:
                yield mol[:i] + rule[1] + mol[i+len(rule[0]):]

def reduce(mol):
    for rule in rules:
        for i in xrange(len(mol)-len(rule[1])+1):
            if mol[i:i+len(rule[1])] == rule[1]:
                yield mol[:i] + rule[0] + mol[i+len(rule[1]):]

class HeapEl(object):
    def __init__(self, val, gen):
        self.val = val
        self.gen = gen
    def __lt__(self, other):
        return len(self.val) < len(other.val)

molecula = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMg'
pq = [HeapEl(molecula, 0)]
used = set()
while True:
    el = heapq.heappop(pq)
    if el.val in used:
        continue
    used.add(el.val)
    print(el.val)
    if el.val == 'e':
        print(el.gen)
        exit(0)
    for rel in reduce(el.val):
       heapq.heappush(pq, HeapEl(rel, el.gen+1))

