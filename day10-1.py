lengths = [97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190]
chain = range(256)

pos = 0
skip = 0
for length in lengths:
   if pos + length < len(chain):
       sublist = chain[pos:pos+length]
   else:
       sublist = chain[pos:]
       sublist += chain[: length - len(sublist)]

   sublist.reverse()

   for c in range(length):
       chainIndex = pos + c
       if pos + c >= len(chain):
           chainIndex -= len(chain)

       chain[chainIndex] = sublist[c]

   pos += length + skip

   while (pos >= len(chain)):
       pos -= len(chain)
   
   skip += 1

#print chain
print chain[0] * chain[1]
