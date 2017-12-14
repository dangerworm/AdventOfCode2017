data = file('day11-data.txt', 'r')
moves = data.read().split(',')

directions = ['n','ne','se','s','sw','nw']
dx = {
    'n':   0,
    'ne':  1,
    'se':  1,
    's':   0,
    'sw': -1,
    'nw': -1
}

dy = {
    'n':   1,
    'ne':  0,
    'se': -1,
    's':  -1,
    'sw':  0,
    'nw':  1
}

x, y = 0, 0
maxX, maxY = 0, 0
for m in moves:
    x += dx[m]
    y += dy[m]

    if x > maxX:
        maxX = x

    if y > maxY:
        maxY = y

print max(maxX, maxY)

