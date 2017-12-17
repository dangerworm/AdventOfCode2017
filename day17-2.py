steps = 356

bfr = [0]
pos = 0

bfr1 = 0
for i in range(1, 30):
    insertPoint = (pos + steps) % len(bfr) + 1
    bfr.insert(insertPoint, i)
    pos = insertPoint

    if bfr[1] != bfr1:
        bfr1 = bfr[1]
        
    output = [i, bfr[1], steps % bfr[1], bfr[1] % steps]
    for o in output:
        print '%10.3f' % o,
    print
    

