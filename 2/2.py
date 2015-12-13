total = 0

for line in open('input.txt'):
    w, l, h = line.split('x')
    w = int(w)
    l = int(l)
    h = int(h)
    #slack = min(w*l,l*h,h*w)
    #total += 2*l*w + 2*w*h + 2*h*l + slack
    bind = 2*min(w+l, l+h, h+w)
    bow = w*l*h
    total += bind + bow

print(total)
