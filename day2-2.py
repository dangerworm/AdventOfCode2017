data = file('day2-data.txt', 'r')

lines = data.read().split('\n')

matrix = []
for line in lines:
    matrix.append([int(x) for x in line.split('\t') if x != ''])

total = 0
for row in matrix:
    for n in row:
        for m in row:
            high = max(n, m)
            low = min(n, m)
            if m%n == 0 and m != n:
                print 'Found %d and %d' % (m, n)
                total += m/n

print total
