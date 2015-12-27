conts = []
for line in open('input.txt'):
    conts.append(int(line.strip()))

def bitsTomask(bits):
    return [1 if (bits >> i) & 0x01 else 0 for i in xrange(len(conts))]

res = dict()
amounts = []
for i in xrange(2 ** len(conts)):
    s = sum([x*y for (x,y) in zip(bitsTomask(i), conts)]) 
    amount = sum(bitsTomask(i))
    if s == 150:
        
        res[amount] = res.get(amount, 0) + (1 if s == 150 else 0)
        if amount not in amounts:
            amounts.append(amount)

print(res[min(amounts)])
