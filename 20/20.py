import math
visited = {k:0 for k in xrange(10000000)}
def divs(n):
    for i in xrange(1, int(math.sqrt(n))+1):
        if n % i == 0:
            yield i
            if i != n/i:
                yield n/i
#house = 2000000
house = 1
while True:
    summ = 0
    for d in divs(house):
        if visited[d] < 50:
            summ += d
            visited[d] += 1
    if summ*11 >= 33100000:
        print('result', house)
        exit(0);
    #print(house, summ)
    house += 1

