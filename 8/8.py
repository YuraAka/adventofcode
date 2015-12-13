with open('input.txt') as input:
    code_len = 0
    mem_len = 0
    encode_len = 0
    for line in input:
        code_len += len(line.strip())
        mem_len += eval('len({0})'.format(line.strip()))

        encode_len += len('"' + line.strip().replace('\\', '\\\\').replace('\"', '\\\"') + '"')
    #print code_len, mem_len, code_len - mem_len
    print encode_len - code_len
