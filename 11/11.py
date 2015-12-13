def to_abc(num):
    result = str()
    while True:
        cur = num % 26
        result = chr(cur + ord('a')) + result
        num /= 26
        if not num:
            return result

def from_abc(txt):
    result = 0
    exp = 0
    for l in reversed(txt):
        result += (ord(l)-ord('a')) * (26 ** exp)
        exp += 1

    return result

def has_inc(txt):
    if len(txt) < 3:
        return False
    ords = [ord(l) for l in txt]
    deltas = []
    prev = ords[0]
    for i in xrange(1, len(ords)):
        deltas.append(ords[i]-prev)
        prev = ords[i]
    for i in xrange(1, len(deltas)):
        if [deltas[i-1],deltas[i]] == [1,1]:
            return True
    return False
        
def no_restrict(txt):
    return 'i' not in txt and 'o' not in txt and 'l' not in txt

def has_dup(txt):
    count = 0
    used = set()
    for l in txt:
        if l not in used and l+l in txt:
            count += 1 
            used.add(l)
    return count >=2

#input = 'cqjxjnds'
input = 'cqjxxyzz'
inputd = from_abc(input)
while True:
    inputd += 1
    inpute = to_abc(inputd)
    if has_inc(inpute) and no_restrict(inpute) and has_dup(inpute):
        print(inpute)
        exit()


