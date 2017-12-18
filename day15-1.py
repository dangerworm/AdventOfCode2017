class Generator:
    def __init__(self, start, multiplier):
        self.value = start
        self.multiplier = multiplier

    def getNext(self):
        self.value = (self.value * self.multiplier) % 2147483647
        return self.value

# Initial values
a, b = 277, 349 # Puzzle input
#a, b = 65, 8921 # Test

a = Generator(65, 16807)
b = Generator(8921, 48271)

judgeTotal = 0
#n = 50
n = 40000000
i = 0
while i < n:
    if i % 1000000 == 0:
        print '%dM' % (i/1000000)

    #Remainders
    aR = int(bin(a.getNext())[2:][-16:], 2)
    bR = int(bin(b.getNext())[2:][-16:], 2)
        
    if not aR ^ bR:
        judgeTotal += 1

    i += 1
    
print judgeTotal
