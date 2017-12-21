route = file('day19-data.txt','r').read().split('\n')
route = [list(line) for line in route]

U, R, D, L  = 0, 1, 2, 3

d = [[0, -1], [1, 0], [0, 1], [-1, 0]]

x, y = route[0].index('|'), 0
heading = D

letters = ''
ignore = ['|','-','+']

while True:
    c = route[y][x]

    if c == ' ':
        break

    if c not in ignore:
        letters += c
    
    if route[y][x] != '+':
        x += d[heading][0]
        y += d[heading][1]
    else:
        up = [x, y-1]
        down = [x, y+1]
        left = [x-1, y]
        right = [x+1, y]

        backwards = d[(heading + 2) % 4]

        surroundings = []
        for direction in d:
            if direction[0] == backwards[0] and direction[1] == backwards[1]:
                surroundings.append(' ')
            else:
                s = route[y + direction[1]][x + direction[0]]
                surroundings.append(s)

        #print [i for i in range(4) if surroundings[i] != ' ']
        heading = [i for i in range(4) if surroundings[i] != ' '][0]

        x += d[heading][0]
        y += d[heading][1]

print letters
