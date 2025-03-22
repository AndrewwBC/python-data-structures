## Every list in python as a list of references
## This means that every list uses +/-64 bits for element
## to store the memory address poiting to the real element

## Compact arrays are free of use this 64 bit space in the memory,
## Being more effective for big data

import array, sys

primes = array.array('i', [2, 3, 5, 7, 11, 13, 17,19])

data = []

for k in range(10):
    print(sys.getsizeof(data))
    data.append(None)
