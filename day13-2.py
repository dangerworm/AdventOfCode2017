class Scanner:
    def __init__(self, depth, scanRange):
        self.depth = int(depth)
        self.range = int(scanRange)
        self.pathLength = (self.range - 1) * 2
        self.position = 0

    def move(self, places):
        self.position = places % self.pathLength
        if self.position == self.pathLength:
            self.position = 0

        self.index = self.position
        if self.position >= self.range:
            self.index = self.pathLength - self.position
        
scanners = []
data = file('day13-data.txt', 'r')
index = 0
for d in data.read().split('\n'):
    config = d.split(':')
    while index < int(config[0]):
        scanners.append(Scanner(index, 0))
        index += 1
    scanners.append(Scanner(config[0], config[1]))
    index += 1

maxDepth = max(s.depth for s in scanners) + 1
picoSeconds = 0
while True:
    if (picoSeconds % 100000 == 0):
        print 'nanoseconds:', picoSeconds / 1000

    severity = 0
    for depth in range(maxDepth):
        if scanners[depth].range == 0:
            continue
        scanners[depth].move(picoSeconds + depth)
        if scanners[depth].index == 0:
            severity = 1
            break
        
    if severity == 0:
        break

    picoSeconds += 1

print picoSeconds, 'picoseconds'
