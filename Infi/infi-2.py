data = file('infi-data2.txt', 'r').read()

robots = []
robot = ''
instructions = []
instruction = ''

instruction_list = []

robot_open = False
inst_open = False

num_robots = 0

x = 0
while x < len(data):
    if data[x-1] == '[':
        robot_open = True
    elif data[x] == ']':
        robot_open = False
        robots.append([int(r) for r in robot.split(',')])
        robot = ''

    if data[x-1] == '(':
        inst_open = True
        num_robots = len(robots)
    elif data[x] == ')':
        inst_open = False
        instructions.append([int(i) for i in instruction.split(',')])
        instruction = ''

        if len(instructions) == num_robots:
            instruction_list.append(instructions)
            instructions = []

    if robot_open:
        robot += data[x]
    if inst_open:
        instruction += data[x]

    x += 1

# Code used to find the parameters of the final grid
##total = 0
##min_x, min_y = 0, 0
##max_x, max_y = 0, 0
##for inst in instruction_list:
##    for r in range(num_robots):
##        for d in range(2):
##            robots[r][d] += inst[r][d]
##    
##        if robots[0][0] == robots[1][0] == robots[2][0] and \
##            robots[0][1] == robots[1][1] == robots[2][1]:
##            total += 1
##
##            if robots[0][0] < min_x:
##                min_x = robots[0][0]
##            if robots[0][1] < min_y:
##                min_y = robots[0][1]
##
##            if robots[0][0] > max_x:
##                max_x = robots[0][0]
##            if robots[0][1] > max_y:
##                max_y = robots[0][1]

matrix = []
for y in range(29):
    matrix.append(list(' '*47))

for inst in instruction_list:
    for r in range(num_robots):
        for d in range(2):
            robots[r][d] += inst[r][d]
    
        if robots[0][0] == robots[1][0] == robots[2][0] and \
            robots[0][1] == robots[1][1] == robots[2][1]:
            matrix[robots[0][1]][robots[0][0]] = '*'

for line in matrix:
    print ''.join(line)
