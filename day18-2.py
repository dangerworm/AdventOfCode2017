class Interpreter:
    def __init__(self, p):
        self.freq = 0
        self.counter = 0
        self.instructions = {}
        self.registers = {}
        self.set('p', p)

    def addInstruction(self, i, instruction):
        self.instructions[i] = instruction

    def snd(self, x):
        if not self.isNumeric(x):
            x = self.registers[x]
        self.freq = x

    def set(self, x, y):
        if x not in self.registers:
            self.registers[x] = 0

        if not self.isNumeric(y):
            y = self.registers[y]
            
        self.registers[x] = y

    def add(self, x, y):
        if x not in self.registers:
            self.registers[x] = 0

        if not self.isNumeric(y):
            y = self.registers[y]
            
        self.registers[x] += y

    def mul(self, x, y):
        if x not in self.registers:
            self.registers[x] = 0

        if not self.isNumeric(y):
            y = self.registers[y]
                
        self.registers[x] *= y

    def mod(self, x, y):
        if x not in self.registers:
            self.registers[x] = 0

        if not self.isNumeric(y):
            y = self.registers[y]

        self.registers[x] %= y

    def rcv(self, x):
        if not self.isNumeric(x):
            x = self.registers[x]
        
        if x == 0:
            pass
        else:
            return 'Recovered', self.freq

    def jgz(self, x, y):
        if not self.isNumeric(x):
            x = self.registers[x]

        if x > 0:
            self.counter += y - 1

    def isNumeric(self, x):
        checkValue = str(x)
        if checkValue[0] == '-':
            checkValue = checkValue[1:]

        value = eval('u"%s"' % checkValue)
        return value.isnumeric()

    def param(self, value):
        checkValue = value
        if value[0] == '-':
            checkValue = value[1:]

        if not eval('u"' + checkValue + '"').isnumeric():
            return '\'%s\'' % value

        return value

    def getNextCommand(self):
        i = self.instructions[self.counter]

        command = 'cpu.%s(%s' % (i[0], cpu.param(i[1]))
        if len(i) > 2:
            command += ', %s' % cpu.param(i[2])
        command += ')'

        self.counter += 1

        return command

p0 = Interpreter(0)
p1 = Interpreter(1)

data = file('day18-data.txt', 'r').read().split('\n')

for i in range(len(data)):
    cpu.addInstruction(i, data[i].split(' '))

output = None
while output == None:
    command = cpu.getNextCommand()

    #print command
    output = eval(command)
    #print cpu.registers, output
   
print output
