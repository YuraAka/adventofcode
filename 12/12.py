import json

def count_list(lst):
    total = 0
    for el in lst:
        if type(el) is int:
            total += el
        elif type(el) is list:
            total += count_list(el)
        elif type(el) is dict:
            total += count_dict(el)
    return total

def count_dict(dct):
    total = 0
    for k, v in dct.iteritems():
        if k == 'red' or v == 'red':
            return 0
        if type(k) is int:
            total += k
        if type(v) is int:
            total += v
        elif type(v) is list:
            total += count_list(v)
        elif type(v) is dict:
            total += count_dict(v)
    return total

input = json.load(open('input.txt'))
print(count_list(input))
