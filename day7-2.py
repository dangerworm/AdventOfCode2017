import re

data = file('day7-data.txt', 'r')
lines = data.read().split('\n')

class Program:
    def __init__(self, text):
        matches = re.match(r"(\D+)\s\((\d+)\)", text)
        self.name = matches.group(1)
        self.weight = int(matches.group(2))
        self.tower = []
        self.towerPrograms = []

    def parseTower(self, text):
        matches = re.match(r"^.+ ->+( \D+)+$", text)
        if not matches == None:
            self.tower = [t.strip() for t in matches.group(1).split(',')]

    def addTowerProgram(self, program):
        self.towerPrograms.append(program)
        self.tower.remove(program.name)

    def getTowerWeight(self):
        return sum([t.getTotalWeight() for t in self.towerPrograms])

    def getTotalWeight(self):
        return self.getTowerWeight() + self.weight

programs = []
programsInTowers = []
for line in lines:
    program = Program(line)
    program.parseTower(line)

    programsInTowers += program.tower
    programs.append(program)

programsInTowers = list(set(programsInTowers))

basePrograms = []
for p in programs:
    if p.name not in programsInTowers:
        basePrograms.append(p)

base = basePrograms[0]
print base.name

tower = []
while sum([len(p.tower) for p in programs]) > 0:
    for leaf in [p for p in programs if len(p.tower) == 0]:
        parent = [p for p in programs if leaf.name in p.tower]
        if (len(parent) > 0):
            parent[0].addTowerProgram(leaf)
    
targetProgram = base
weights = {}
difference = 0
while (targetProgram.towerPrograms) > 0:
    previousWeights = weights
    weightNames = {}
    weights = {}
    for p in targetProgram.towerPrograms:
        weight = p.getTotalWeight()
        weightNames[weight] = p.name
        if weight not in weights:
            weights[weight] = 1
        else:
            weights[weight] += 1

    if len(weights) > 1:
        singleWeight = [w for w in weights if weights[w] == 1][0]
        targetProgram = [p for p in programs if p.name == weightNames[singleWeight]][0]
    else:
        difference = max(previousWeights.keys()) - min(previousWeights.keys())
        print targetProgram.weight - difference
        break
