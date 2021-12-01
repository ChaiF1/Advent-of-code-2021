import numpy as np

file = open("day_1_data.txt")
data = np.loadtxt("day_1_data.txt", delimiter = '\n')

def one(data):
    data_roll = np.roll(data, 1)
    data_roll[0] = 0
    return np.sum(data-data_roll>0)-1 # Subtract 1 as the value at index 0 is always positive but should not be counted
    
  
windows = np.convolve(data, np.ones(3)) 
windows = np.delete(windows, [0, 1, -1, -2])