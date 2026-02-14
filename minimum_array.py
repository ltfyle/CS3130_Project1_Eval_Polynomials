"""
Find the minimum of an array

problem type: selection

brute force:
min = A[0]
if min>A[i], min = A[i]
else: iteration

iteration:
compare min and A[i+1] until i==n-1, return min
"""
import numpy as np

array = np.random.randint(1,50,10,int)

min = array[0]
print(array)
print(min)
for i in range(0,len(array)):
    if min > array[i]:
        min = array[i]
print(min)


