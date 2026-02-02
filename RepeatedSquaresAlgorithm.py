"""
Parameters: x, n 

Evaluates a polynomial of n degrees of the form 1 + x + ...+ n*x^n at the point, x, using the repeated squares method.

Returns: p


RepeatedSquaresAlgorithm(x,n)

declares p = 1


for i <- 0 to n:

...

p = p+i*_____

return p

RepeatedSquaresAlgorithm(3,5)
"""
blocks=[1,3,3*3,3*3*3,3*3*3*3,3*3*3*3*3]
print(len(blocks))

p=1
for i in range(0,6):
    p=p+(i*blocks[i])
print(p)
    