def nice(word):
    vowels = 0
    doubles = False
    prev = None
    for l in word:
        if l in 'aeiou':
            vowels += 1
        if prev and prev == l:
            doubles = True
        prev = l

    if vowels < 3 or not doubles:
        return False

    return not('ab' in word or 'cd' in word or 'pq' in word or 'xy' in word)

def nice2(word):
    if len(word) < 3:
        return False
    dups = False
    for i in xrange(0, len(word)-1):
        if word.count(word[i:i+2]) > 1:
            dups = True
            break
    if not dups:
        return False

    for i in xrange(2, len(word)):
        if word[i-2] == word[i]:
            return True
    return False        

with open('input.txt') as input:
    count = 0
    for word in input:
         count += 1 if nice2(word) else 0

print(count)
