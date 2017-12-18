from math import log

class Generator:
    def __init__(self, start, multiplier, divisor):
        self.value = start
        self.multiplier = multiplier
        self.divisor = divisor

    def getNext(self):
        self.generate()
        while self.value % self.divisor != 0:
            self.generate()
        return self.value

    def generate(self):
        self.value = (self.value * self.multiplier) % 2147483647

# Initial values
a, b = 277, 349 # Puzzle input
#a, b = 65, 8921 # Test

a = Generator(a, 16807, 4)
b = Generator(b, 48271, 8)

judgeTotal = 0
#n = 5
n = 5000000
i = 0
while i < n:
    if i % 100000 == 0:
        print '%d' % i

    #Remainders
    x = a.getNext()
    y = b.getNext()
    aR = int(bin(x)[2:][-16:], 2)
    bR = int(bin(y)[2:][-16:], 2)
    
    if not aR ^ bR:
        judgeTotal += 1

    i += 1
    
print judgeTotal
