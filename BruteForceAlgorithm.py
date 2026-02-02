'''
Parameters: x, n both type int
Returns: p

Evaluates a polynomial with n degrees at point x, using the *Brute Force Evaluation Method*

Declare p = 0.0
Declare power = 1

for i <- 0 to n do
    power <- 1
    for j <- 1 to n do
        power <- power*x
    p = p+(n*power)

return p
'''

import timeit
def BruteForceAlgorithm(x: int, n: int):

    p = 1

    for i in range(0,n+1):

        power = 1     
        for j in range(1,i+1):
                power = power * x


        p = p + (i*power) 
        
    
    return p 


BruteForceAlgorithm(123,2500)
