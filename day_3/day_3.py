import numpy as np
bits = np.genfromtxt("day_3_data.txt", delimiter = 1, dtype=int)

def calc_mcv(row):
    return round(np.sum(row)/len(row)+1)-1 # I always want 0.5 to round up so as Python uses banker rounding I have to add and subtract 1

def array_to_decimal(array):
    return int(np.array_str(array)[1:-1].replace(' ', ''), 2) # Converting numpy array to decimal number

def one(data):
    bit = ''
    data_t = np.transpose(data)
    for row in data_t:
        bit += str(calc_mcv(row))
    gamma = int(bit, 2)
    epsilon = 2**len(data_t[:,0])+~int(bit, 2) # epsilon is a bit flip of gamma, but using the not function makes epsilon negative so have to make it positive first by adding 2**len(data[:,0])
    return gamma*epsilon    

def two(data, a): # a = 0 calculates OGR, a = 1 calculates csr
    col = 0
    while len(data) != 1:
        value = a + ((-1)**a)*calc_mcv(data[:,col])
        """ 
        When a = 0: value = calc_mcv(data[:,col])
        when a = 1: value = 1-calc_mcv(data:,col) which causes to flip 1 to 0 and 0 to 1, which is swapping the mcv and lcv value. 
            Make sure to still round the mcv up as when we get the same amount of 1s and 0s we want to see that value = 1-1.
        """
        data = np.delete(data, np.argwhere(np.transpose(data)[col] != value), 0) # Remove rows where most common value is not present
        col += 1 # Move on to next column
    return array_to_decimal(data[0])

print(one(bits))
print(two(bits, 0)*two(bits, 1))