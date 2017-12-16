data = file('jumps.txt', 'r')
jumps = [int(j) for j in data.read().split('\n')]
pos = 0
steps = 0
while pos > -1 and pos < len(jumps):
    nextPos = pos + jumps[pos]
    if jumps[pos] > 2:
        jumps[pos] -= 1
    else:
        jumps[pos] += 1
    pos = nextPos
    steps += 1

print steps
