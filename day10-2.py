data = '97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190'
lengths = [ord(c) for c in data]
lengths += [17,31,73,47,23]
chain = range(256)

pos = 0
skip = 0
for x in range(64):
   for length in lengths:
       if pos + length < len(chain):
           sublist = chain[pos:pos+length]
       else:
           sublist = chain[pos:]
           sublist += chain[:length - len(sublist)]

       sublist.reverse()

       for c in range(length):
           chainIndex = pos + c
           while chainIndex >= len(chain):
               chainIndex -= len(chain)

           chain[chainIndex] = sublist[c]

       pos += length + skip

       while (pos >= len(chain)):
           pos -= len(chain)
       
       skip += 1

denseHash = []
for y in range(16):
   result = chain[16*y]
   for z in range(1,16):
      result ^= chain[(16*y)+z]

   hexChars = '00' + hex(result)[2:]
   denseHash.append(hexChars[-2:])

print ''.join(denseHash)
