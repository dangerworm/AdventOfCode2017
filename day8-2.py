data = file('day8-data.txt', 'r')
lines = data.read().split('\n')

operators = {}
operators['inc'] = '+'
operators['dec'] = '-'

registers = {}
instructions = []
for line in lines:
    s = line.split()
    if len(s) == 0:
        continue
    
    registers[s[0]] = 0
    instructions.append(s[3] + ' ' + \
                        'registers[\'' + s[4] + '\'] ' + \
                        ' '.join(s[5:]) + ': ' + \
                        'registers[\'' + s[0] + '\'] ' + \
                        operators[s[1]] + '= ' + s[2])

highest = -1000000
for i in instructions:
    #print i
    exec i
    if max(registers.values()) > highest:
        highest = max(registers.values())

for r in registers:
    print r, registers[r]

print 'Current max: ', max(registers.values())
print 'Highest max: ', highest
