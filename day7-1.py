import re

data = file('day7-data.txt', 'r')
lines = data.read().split('\n')

class Program:
   def __init__(self, text):
       matches = re.match(r"(\D+)\s\((\d+)\)", text)
       self.name = matches.group(1)
       self.weight = matches.group(2)
       self.tower = []
       self.programs = []

   def parseTower(self, text):
       matches = re.match(r"^.+ ->+( \D+)+$", text)
       if not matches == None:
           self.tower = [t.strip() for t in matches.group(1).split(',')]

   def addProgram(self, program):
       self.programs.append(program)

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
