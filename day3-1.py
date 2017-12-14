address = 265149

side = 1
while side * side < address:
    side += 2

#print 'Side:', side
matrix = []
for y in range(side):
    matrix.append([0] * side)

middle = side / 2
x = side / 2
y = side / 2

n = 1
matrix[y][x] = n
n += 1

directions = [[1,0],[0,-1],[-1,0],[0,1]] # right, up, left, down
direction = 0

dataX = -1
dataY = -1
for distance in range(1,side):
    for d in range(2):
        for dx in range(distance):
            x += directions[direction%4][0]
            y += directions[direction%4][1]
            matrix[y][x] = n
            if (n == address):
                dataX = x
                dataY = y
            n += 1
        direction += 1

while x < side - 1:
    x += directions[direction%4][0]
    matrix[y][x] = n #1
    if (n == address):
        dataX = x
        dataY = y
    n += 1

#for row in matrix:
#    for col in row:
#        print '%5d' % col,
#    print

diffX = abs(dataX - middle)
diffY = abs(dataY - middle)

print diffX + diffY
