#banks = [0,2,7,0]
banks = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
memory = []

loops = 0
while banks not in [m[0] for m in memory]:
   memory.append([banks[:], loops])
   #print memory
   i = banks.index(max(banks))
   blocks = banks[i]
   banks[i] = 0

   while blocks > 0:
       i += 1
       if i == len(banks):
           i = 0

       banks[i] += 1
       blocks -= 1

   loops += 1

print loops
