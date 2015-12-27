import re
def distx(fly_speed, fly_time, rest_time, finish_time):
    intervals = finish_time / (fly_time+rest_time)
    lastint = finish_time % (fly_time+rest_time)
    return (intervals*fly_time + min(lastint, fly_time)) * fly_speed

def oldscore():
    with open('input.txt') as input:
        m = re.compile('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
        total = 2503
        maxdist = 0
        for line in input:
            g = m.match(line)
            name = g.group(1)
            fly_speed = int(g.group(2))
            fly_time = int(g.group(3))
            rest_time = int(g.group(4))
            print ('Name: {0}, speed: {1}, time: {2}, rest: {3}'.format(name, fly_speed, fly_time, rest_time))
            intervals = total / (fly_time+rest_time)
            print('Int: {0}'.format(intervals))
            lastint = total % (fly_time+rest_time)
            dist = (intervals*fly_time + min(lastint, fly_time)) * fly_speed
            print('Dist: {0}'.format(dist))
            maxdist = max(maxdist, dist)

    print(maxdist)

def newscore():
    with open('input.txt') as input:
        m = re.compile('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
        total = 2503
        scores = []
        ttx = []
        for line in input:
            g = m.match(line)
            name = g.group(1)
            fly_speed = int(g.group(2))
            fly_time = int(g.group(3))
            rest_time = int(g.group(4))
            scores.append(0)
            ttx.append((fly_speed, fly_time, rest_time))

        for i in xrange(total):
            best = max([distx(t[0], t[1], t[2], i+1) for t in ttx])
            for j in xrange(len(ttx)):
                if best == distx(ttx[j][0], ttx[j][1], ttx[j][2], i+1):
                    scores[j] += 1

        print(max(scores))
                
newscore()
