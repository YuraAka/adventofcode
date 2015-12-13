import hashlib
import sys

postfix = 0
while True:
    base = 'yzbqklnj' + str(postfix)
    m = hashlib.md5()
    m.update(base)
    if m.hexdigest().startswith('000000'):
        print(postfix)
        exit()
    postfix += 1
