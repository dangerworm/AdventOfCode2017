data = file('day16-data.txt', 'r').read()

initialOrder = 'abcdefghijklmnop'
programs = list(initialOrder)

moves = data.split(',')

# By experimentation, I've found that
# the programs return to their initial
# order after 48 moves.



counter = 0
while counter < 16: # 1000000000 / 48 = 16 (see below)
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

    counter += 1

    # By experimentation, we find that the
    # programs return to their initial
    # order after 48 moves.

    # 1000000000 / 48 = 16

    if ''.join(programs) == initialOrder:
        print counter
        break

print ''.join(programs)
