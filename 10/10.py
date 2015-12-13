import sys
input = '1113222113'

for i in xrange(50):
    result = ''
    count = 0
    prev = None
    for c in input:
        if prev is not None and prev != c:
            result += str(count)
            result += prev
            count = 1
            prev = c
        else:
            prev = c
            count += 1
    result += str(count)
    result += prev
    input = result

print(len(input))
