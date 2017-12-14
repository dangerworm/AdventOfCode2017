address = 265149
#address = 256

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
firstLarger = -1
for distance in range(1,side):
    for d in range(2):
        for dx in range(distance):
            x += directions[direction%4][0]
            y += directions[direction%4][1]

            # Get sum of adjacent values, going clockwise from left
            total = 0
            if x-1 >= 0: # Left
                total += matrix[y][x-1]
            if y-1 >= 0 and x-1 >= 0: # Top left
                total += matrix[y-1][x-1]
            if y-1 >= 0: # Top
                total += matrix[y-1][x]
            if y-1 >= 0 and x+1 < side: # Top right
                total += matrix[y-1][x+1]   
            if x+1 < side: # Right
                total += matrix[y][x+1]
            if y+1 < side and x+1 < side: # Bottom right
                total += matrix[y+1][x+1]
            if y+1 < side: # Bottom
                total += matrix[y+1][x]
            if y+1 < side and x-1 >= 0: # Bottom left
                total += matrix[y+1][x-1]

            matrix[y][x] = total
            if firstLarger == 0:
                firstLarger = total
                #print firstLarger
            
            if (n == address):
                dataX = x
                dataY = y

            if (firstLarger == -1 and total > address):
                firstLarger = total

            n += 1
        direction += 1

while x < side - 1:
    x += directions[direction%4][0]
    # Get sum of adjacent values, going clockwise from left
    total = 0
    if x-1 >= 0: # Left
        total += matrix[y][x-1]
    if y-1 >= 0 and x-1 >= 0: # Top left
        total += matrix[y-1][x-1]
    if y-1 >= 0: # Top
        total += matrix[y-1][x]
    if y-1 >= 0 and x+1 < side: # Top right
        total += matrix[y-1][x+1]   
    if x+1 < side: # Right
        total += matrix[y][x+1]
    if y+1 < side and x+1 < side: # Bottom right
        total += matrix[y+1][x+1]
    if y+1 < side: # Bottom
        total += matrix[y+1][x]
    if y+1 < side and x-1 >= 0: # Bottom left
        total += matrix[y+1][x-1]

    matrix[y][x] = total
    if firstLarger == 0:
        firstLarger = total
        #print firstLarger
    
    if (n == address):
        dataX = x
        dataY = y

    if (firstLarger == -1 and total > address):
        firstLarger = total

    n += 1

print firstLarger
