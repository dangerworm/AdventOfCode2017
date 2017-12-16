class Generator:
    def __init__(self, startingValue, factor):
        self.startingValue = startingValue
        self.previousValue = startingValue
        self.factor = factor
        self.divisor = 2147483647

    def getNext(self):
        product = self.previousValue * self.factor
        remainder = product % self.divisor
        self.previousValue = product
        return remainder

a = Generator(65, 16807)
b = Generator(8921, 48271)

judgeTotal = 0
#n = 5
n = 40000000
i = 0
while i < n:
    if i % 1000 == 0:
        print i
    
    aNext, bNext = a.getNext(), b.getNext() 
    #print '%16d %16d' % (aNext, bNext)

    if aNext == a.startingValue:
        print 'a reached its starting value'
        break
    if bNext == b.startingValue:
        print 'b reached its starting value'
        break

    n1 = bin(aNext)[-16:]
    n2 = bin(bNext)[-16:]

    if n1 == n2:
        judgeTotal += 1

    i += 1
    
print judgeTotal
