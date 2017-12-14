data = file('day2-data.txt', 'r')

lines = data.read().split('\n')

matrix = []
for line in lines:
    matrix.append([int(x) for x in line.split('\t') if x != ''])

total = 0
for row in matrix:
    high = max(row)
    low = min(row)
    diff = high - low
    total += diff

print total
