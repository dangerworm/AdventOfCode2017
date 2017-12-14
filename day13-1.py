class Scanner:
    def __init__(self, depth, scanRange):
        self.depth = int(depth)
        self.range = int(scanRange)
        self.pathLength = (self.range - 1) * 2
        self.reset()

    def reset(self):
        self.position = 0
        self.index = 0

    def move(self):
        self.position += 1
        if self.position == self.pathLength:
            self.position = 0

        self.index = self.position
        if self.position >= self.range:
            self.index = self.pathLength - self.position

    def moveN(self, places):
        self.position += (self.position + places) % self.pathLength
        if self.position == self.pathLength:
            self.position = 0

        self.index = self.position
        if self.position >= self.range:
            self.index = self.pathLength - self.position

    def toString(self):
        return 'depth:', self.depth, 'index:', self.index

##scanners.append(Scanner(0,3))
##scanners.append(Scanner(1,2))
##scanners.append(Scanner(4,4))
##scanners.append(Scanner(6,4))
        
data = file('day13-data.txt', 'r')
scanners = []
for d in data.read().split('\n'):
    config = d.split(':')
    scanners.append(Scanner(config[0], config[1]))

maxDepth = max(s.depth for s in scanners) + 1
severity = 0
for depth in range(maxDepth):
    #print 'depth:', depth
    localScanners = [s for s in scanners if s.depth == depth and s.index == 0]
    if len(localScanners) > 0:
        scanner = localScanners[0]
        #print 'scanner:', scanner.depth
        severity += scanner.depth * scanner.range
    
    for s in scanners:
        s.move()

print severity
