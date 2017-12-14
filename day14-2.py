key = 'hxtvlmkl'
#key = 'flqrgnkx'

def knotHash(token):
    lengths = [ord(c) for c in token]
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

    return ''.join(denseHash)

tokens = []
for i in range(128):
    tokens.append(key + '-' + str(i))

binaryRows = []
for token in tokens:
    knotted = knotHash(token)
    left = knotted[::2]
    right = knotted[1::2]
    values = []
    for i in range(len(left)):
        values.append('0x' + left[i] + right[i])

    shortBinary = ['0000000' + bin(int(v, 0))[2:] for v in values]
    longBinary = [b[-8:] for b in shortBinary]

    binaryRows.append(''.join(longBinary))

total = 0
rows = []
for binaryRow in binaryRows:
    row = ['.' if col == '0' else '#' for col in binaryRow]
    #print ''.join(row)
    rows.append(''.join(row))
    total += sum([int(col) for col in binaryRow])

for row in rows:
    print row

print rows[4][4]
