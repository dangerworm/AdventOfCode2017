data = file('jumps.txt', 'r')
jumps = [int(j) for j in data.read().split('\n')]
pos = 0
steps = 0
while pos > -1 and pos < len(jumps):
    nextPos = pos + jumps[pos]
    jumps[pos] += 1
    pos = nextPos
    steps += 1

print steps
