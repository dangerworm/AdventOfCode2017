data = file('day16-data.txt', 'r').read()

initialOrder = 'abcdefghijklmnop'
programs = list(initialOrder)

moves = data.split(',')

for move in moves:
    op = move[0]

    if op == 's':
        i = int(move[1:])
        programs = programs[-i:] + programs[:-i]
        continue

    o1, o2 = move[1:].split('/')
    if op == 'p':
        i1 = programs.index(o1)
        i2 = programs.index(o2)
    elif op == 'x':
        i1, i2 = [int(i) for i in move[1:].split('/')]

    tmp = programs[i1]
    programs[i1] = programs[i2]
    programs[i2] = tmp

print ''.join(programs)
