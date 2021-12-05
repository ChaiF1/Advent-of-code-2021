import numpy as np
file = open("day_5_data.txt", "r")

lines = np.empty((0, 2,2), dtype=int)
field = np.zeros((1000,1000), dtype=int)

def one(p1, p2):
    global field
    delta_x = p2[0]-p1[0]
    delta_y = p2[1]-p1[1]
    if delta_x == 0:
        field[min(p1[1], p2[1]):max(p1[1], p2[1])+1, p1[0]] += 1
    elif delta_y == 0:
        field[p1[1], min(p1[0], p2[0]):max(p1[0], p2[0])+1] += 1
    else:
        for k in range(abs(delta_y)+1):
            field[p1[1]+np.sign(delta_y)*k, p1[0]+np.sign(delta_x)*k] += 1

for line in file:
    test = line.split(' -> ')
    p1 = eval(test[0])
    p2 = eval(test[1])
    one(p1, p2)

print(field)
print(np.sum(field>1))