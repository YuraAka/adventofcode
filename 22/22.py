import copy
initstate = {
    'hp' : 50,
    'mp' : 500,
    'def': 0,
    'bhp': 51,
    'bdm': 9,
    'spells' : {},
    'wasted' : 0,
    'depth' : 0
}

result = 50000000

def xprint(*_):
    pass

def drain(state):
    if state['mp'] < 73:
        return False
    state['mp'] -= 73
    state['bhp'] -= 2
    state['hp'] += 2
    state['wasted'] += 73
    xprint('drain')
    return True

def magicmissile(state):
    if state['mp'] < 53:
        return False
    state['mp'] -= 53
    state['bhp'] -= 4
    state['wasted'] += 53
    xprint('missile')
    return True

def shield(state):
    if 'shield' in state['spells'] or state['mp'] < 113:
        return False
    state['mp'] -= 113
    state['def'] += 7
    def do(state): xprint('shild'); state['def'] = 7
    state['spells']['shield'] = (6, do)
    state['wasted'] += 113
    return True

def poison(state):
    if 'poison' in state['spells'] or state['mp'] < 173:
        return False
    state['mp'] -= 173
    def do(state): xprint('poison'); state['bhp'] -= 3
    state['spells']['poison'] = (6, do)
    state['wasted'] += 173
    return True

def recharge(state):
    if 'recharge' in state['spells'] or state['mp'] < 229:
        return False
    state['mp'] -= 229
    def do(state): xprint('recharge'); state['mp'] += 101
    state['spells']['recharge'] = (5, do)
    state['wasted'] += 229
    return True

def applyeffects(state):
    todel = []
    state['def'] = 0
    for name in state['spells'].iterkeys():
        time, onaction = state['spells'][name]
        time -= 1
        if onaction: onaction(state)
        if time == 0:
            todel.append(name)
        else:
            state['spells'][name] = (time, onaction)
    for name in todel:
        del state['spells'][name]

def userturn(state):
    global result
    state['hp'] -= 1
    applyeffects(state)
    xprint ('user turn: ', state)
    if state['bhp'] <= 0:
        if state['wasted'] < result:
            print(state['wasted'])
        result = min(result, state['wasted'])
        xprint('==> win after', state['depth'])
        return
    if state['hp'] <= 0:
        return
    newstate = copy.deepcopy(state)
    newstate['depth'] += 1
    #for skill in (shield, recharge, poison, drain, magicmissile):
    for skill in (drain, shield, magicmissile, poison, recharge):
        if not skill(newstate):
            continue
        if newstate['bhp'] <= 0:
            if newstate['wasted'] < result:
                print(newstate['wasted'])
            result = min(result, newstate['wasted'])
            xprint('==> win after', newstate['depth'])
        else:
            bossturn(newstate)
        newstate = copy.deepcopy(state)
        newstate['depth'] += 1

def bossturn(state):
    global result
    applyeffects(state)
    xprint('boss turn:', state)
    if state['bhp'] <= 0:
        if state['wasted'] < result:
            print(state['wasted'])
        result = min(result, state['wasted'])
        xprint('==> win after', state['depth'])
        return
    if state['hp'] <= 0:
        return
    state['hp'] -= state['bdm'] - state['def']
    if state['hp'] > 0:
        userturn(state)
    else:
        xprint('==> lose after', state['depth'])

userturn(initstate)
print(result)

