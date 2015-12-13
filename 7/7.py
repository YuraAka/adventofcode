input = open('in.txt')
output = open('out.py', 'w+')

def opstr(op):
    if op == 'RSHIFT': return '>>'
    if op == 'LSHIFT': return '<<'
    if op == 'OR': return '|'
    if op == 'AND': return '&'
    if op == 'NOT': return '~'
    raise RuntimeError('Unknown {0}'.format(op))


def funstr(fun):
    return '{0}_fn'.format(fun)


def topython(line):
    line.strip()
    body, result = line.split('->')
    fun_name = funstr(result.strip())
    fun_body = '''
def {name}():
    result = precalc.get(\'{name}\')
    if result is None:
        result = {calc}
        precalc[\'{name}\'] = result
    return result
'''
    calc = str()
    for part in body.strip().split(' '):
        if part.isupper():
            calc += opstr(part) + ' '
        elif part.islower():
            calc += funstr(part) + '() '
        else:
            calc += part + ' '
            
    return fun_body.format(name=fun_name, calc=calc) 

with open('in.txt') as input, open('out.py', 'w+') as output:
    output.write('precalc = dict()')
    for line in input:
        output.write(topython(line) + '\n')

    output.write('print(a_fn())\n')

import out
