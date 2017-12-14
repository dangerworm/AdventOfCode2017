class Village:
    def __init__(self, villageId, connections):
        self.id = villageId
        self.connections = connections

    def connectsTo(self, villageId):
        return villageId in self.connections

    def toString(self):
        connections = [str(c) for c in self.connections]
        return str(self.id) + ' <-> ' + ', '.join(connections)
    
data = file('day12-data.txt', 'r')
lines = data.read().split('\n')

villages = []
for l in lines:
    left, right = l.split(' <-> ')

    villageId = int(left)
    connections = [int(r) for r in right.split(', ')]

    villages.append(Village(villageId, connections))

groups = []
for v in villages:
    active = [v.id]
    visited = []

    grouped = []
    for g in groups:
        grouped += g

    if v.id in grouped:
        continue
    
    while len(active) > 0:
        a = active[0]
        visited.append(a)
        if a in active:
            active.remove(a)

        for v in villages:
            if v.connectsTo(a):
                #print str(v.id) + ' connects to ' + str(a)
                active.append(v.id)

        active = list(set([x for x in active if x not in visited]))
            
        #print active
        #print visited
        #raw_input()

    connected = list(set(active + visited))
    if connected not in groups:
        groups.append(connected)

print len(groups)
