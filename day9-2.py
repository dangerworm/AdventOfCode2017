dataFile = file('day9-data.txt', 'r')

##a = '<>' # 0 characters.
##b = '<random characters>' # 17 characters.
##c = '<<<<>' # 3 characters.
##d = '<{!>}>' # 2 characters.
##e = '<!!>' # 0 characters.
##f = '<!!!>>' # 0 characters.
##g = '<{o"i!a,<{i<a>' # 10 characters.

data = dataFile.read()

isGarbage = False
level = 0
total = 0
garbage = 0
i = 0
while i < len(data): 
    c = data[i]

    if c == '!':
        i += 2
        continue
    elif c == '>':
        isGarbage = False

    if not isGarbage:
        if c == '<':
            isGarbage = True
        elif c == '{':
            level += 1
        elif c == '}':
            total += level
            level -= 1
    else:
        garbage += 1

    i += 1

print garbage
