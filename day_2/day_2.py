import numpy as np
data = np.loadtxt("day_2_data.txt", dtype={'names':('col1', 'col2'), 'formats':('U10','i4')})
conv = {'forward':0, 'down':1, 'up':-1}

def one(): 
    horizontal = 0
    depth = 0
    for command in data:
        horizontal += (1-abs(conv[command[0]]))*command[1]
        depth += conv[command[0]]*command[1]
    print(horizontal*depth)
    
def two():
    horizontal = 0
    depth = 0
    aim = 0
    for command in data:
        horizontal += (1-abs(conv[command[0]]))*command[1]
        depth += (1-abs(conv[command[0]]))*command[1]*aim
        aim += conv[command[0]]*command[1]
    print(horizontal*depth)
