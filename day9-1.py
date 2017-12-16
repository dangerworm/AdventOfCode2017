dataFile = file('day9-data.txt', 'r')

##a = '{}' # 1
##b = '{{{}}}' # 1 + 2 + 3 = 6.
##c = '{{},{}}' # 1 + 2 + 2 = 5.
##d = '{{{},{},{{}}}}' # 1 + 2 + 3 + 3 + 3 + 4 = 16.
##e = '{<a>,<a>,<a>,<a>}' # 1.
##f = '{{<ab>},{<ab>},{<ab>},{<ab>}}' # 1 + 2 + 2 + 2 + 2 = 9.
##g = '{{<!!>},{<!!>},{<!!>},{<!!>}}' # 1 + 2 + 2 + 2 + 2 = 9.
##h = '{{<a!>},{<a!>},{<a!>},{<ab>}}' # 1 + 2 = 3.

data = dataFile.read()

isGarbage = False
level = 0
total = 0
i = 0
while i < len(data): 
    c = data[i]

    if c == '!':
        i += 1
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

    i += 1

print total
