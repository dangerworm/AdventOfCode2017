steps = 356

pos = 0
bfr = [0]

for i in range(1, 2018):
    insertPoint = (pos + steps) % len(bfr) + 1
    bfr.insert(insertPoint, i)
    pos = insertPoint
    
i = bfr.index(2017)

print bfr[i+1]
