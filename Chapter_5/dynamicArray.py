## allocate a new array
## set Bi=Ai, for i = 0... n -1
## Set A = B and pray for garbage collector

import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def __len__(self):
        return self._n 
    
    def __getitem__(self, k):
        
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        
        return self._A[k]

    def append(self, obj):
        
        if self._n == self. capacity:
            self.resize(2 * self. capacity)
            self._A[self. n] = obj
            self._n += 1
        
    def _resize(self, c):
        
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
            self._A = B
            self._capacity = c 
    
    def _make_array(self, c):
        return (c * ctypes.py_object)()